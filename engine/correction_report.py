
"""
IELTS Speaking Detailed Correction Report Generator
Uses LLM API (Deepseek) to analyze responses against official IELTS Band Descriptors.
"""
import os, datetime, re
from fpdf import FPDF

# Official descriptors reference (for PDF display)
BAND_DESCRIPTORS_REF = {
    "fluency_coherence": {
        9: "Fluent with only very occasional repetition. Sustained use of accurate language. Any hesitation only to prepare content.",
        7: "Keeps going and readily produces long turns. Uses a range of connectives. Some hesitation, repetition or self-correction.",
        5: "Usually able to keep going, but relies on repetition/self-correction. Hesitations for basic lexis and grammar."
    },
    "lexical_resource": {
        9: "Total flexibility and precise use in all contexts.",
        7: "Resource sufficient to discuss topics at length. Good paraphrasing. Uses some less common vocabulary.",
        5: "Resource sufficient for familiar topics but limited flexibility."
    },
    "grammatical_range": {
        9: "Structures are precise and accurate at all times.",
        7: "Mix of short and complex sentence forms. Frequent error-free sentences. Good control.",
        5: "Basic sentence forms fairly well controlled."
    },
    "pronunciation": {
        9: "Full range of phonological features. Effortlessly understood.",
        7: "Range of features, control variable. Chunking generally appropriate.",
        5: "Some features of band 4 and some of band 6."
    },
    "task_achievement": {
        9: "Fully addresses all parts with well-developed, relevant responses.",
        7: "Addresses all parts. Well-developed responses with relevant supporting detail.",
        5: "Addresses task only partially. Mainly relevant but may lack detail."
    }
}

CRITERION_NAMES = {
    "fluency": "Fluency & Coherence",
    "vocabulary": "Lexical Resource (Vocabulary)",
    "grammar": "Grammatical Range & Accuracy",
    "pronunciation": "Pronunciation",
    "task_achievement": "Task Achievement"
}


def _clean_text(text):
    """Remove or replace characters not suitable for PDF fonts."""
    if not text:
        return text
    repl = {"\u2705": "[PASS] ", "\u274c": "[FAIL] ", "\u26a0\ufe0f": "[WARN] ", "\ufe0f": ""}
    for ch, r in repl.items():
        text = text.replace(ch, r)
    out = [ch for ch in text if ord(ch) < 0x10000]
    return "".join(out)


def _llm_analyze_response(part, question_info, user_response, topic=""):
    """Call LLM API to get detailed IELTS correction analysis."""
    from engine.sample_answers import _call_llm

    # Build question text
    if isinstance(question_info, dict):
        if "cue_card" in question_info:
            q_text = "Cue Card: " + question_info.get("cue_card", "")
            prompts = question_info.get("prompts", [])
            if prompts:
                q_text += "\nPrompts:\n" + "\n".join("- " + p for p in prompts)
        else:
            q_text = str(question_info)
    elif isinstance(question_info, list):
        q_text = "\n".join(question_info)
    else:
        q_text = str(question_info)

    part_desc = {1: "Part 1 - Short personal questions (30-45s)", 2: "Part 2 - Long turn cue card (1-2 min)", 3: "Part 3 - Abstract discussion (45-60s)"}
    part_label = part_desc.get(part, "Part " + str(part))

    system_prompt = (
        "You are an expert IELTS examiner with 20+ years of experience. "
        "Analyze the student's speaking response against official IELTS Band Descriptors. "
        "Write all Analysis sections in Chinese. Official Level descriptions keep in English. Return your analysis in the EXACT structured format below."
    )

    user_prompt = (
        "=== IELTS SPEAKING TEST ===\n"
        + part_label + "\n\n"
        + "=== QUESTION ===\n"
        + q_text + "\n\n"
        + "=== STUDENT'S RESPONSE ===\n"
        + (user_response if user_response else "[No response]") + "\n\n"
        + "=== TASK ===\n"
        + "Analyze this response and provide scores and feedback for each criterion.\n\n"
        + "Return your analysis using this EXACT format:\n\n"
        + "---OVERALL---\n"
        + "Overall Band: [X.X]\n"
        + "Duration Assessment: [adequate/too short]\n\n"
        + "---FLUENCY---\n"
        + "Score: [1-9]\n"
        + "Analysis: [2-3 sentences in Chinese, analyzing the response]\n"
        + "Official Level: [quoted band descriptor for this score level]\n\n"
        + "---VOCABULARY---\n"
        + "Score: [1-9]\n"
        + "Analysis: [2-3 sentences in Chinese]\n"
        + "Official Level: [quoted band descriptor]\n\n"
        + "---GRAMMAR---\n"
        + "Score: [1-9]\n"
        + "Analysis: [2-3 sentences in Chinese]\n"
        + "Official Level: [quoted band descriptor]\n\n"
        + "---PRONUNCIATION---\n"
        + "Score: [1-9]\n"
        + "Analysis: [2-3 sentences in Chinese]\n"
        + "Official Level: [quoted band descriptor]\n\n"
        + "---TASK_ACHIEVEMENT---\n"
        + "Score: [1-9]\n"
        + "Analysis: [2-3 sentences in Chinese]\n"
        + "Official Level: [quoted band descriptor]\n\n"
        + "---RECOMMENDATIONS---\n"
        + "[3-5 specific, actionable recommendations]\n\n"
        + "IMPORTANT: Write Analysis sections in Chinese. Official Level in English. Be accurate. Use ONLY the EXACT section headers shown above."
        + " Each section header starts with --- and ends with ---."
    )

    raw = _call_llm(system_prompt, user_prompt)
    if raw.startswith("[ERROR]"):
        return None, raw
    return raw, None


def _parse_llm_response(raw):
    """Parse the structured LLM response into a dict."""
    result = {
        "overall_band": 0, "scores": {}, "analyses": {}, "descriptors": {}, "recommendations": []
    }
    if not raw:
        return result

    # Extract scores
    for key in ["FLUENCY", "VOCABULARY", "GRAMMAR", "PRONUNCIATION", "TASK_ACHIEVEMENT"]:
        m = re.search(r"---" + key + r"---\s*\nScore:\s*([0-9.]+)", raw, re.IGNORECASE)
        if m:
            result["scores"][key.lower()] = float(m.group(1))
        m2 = re.search(r"---" + key + r"---\s*\nScore:\s*([0-9.]+).*?\nAnalysis:\s*(.+?)\n", raw, re.DOTALL | re.IGNORECASE)
        if m2:
            result["analyses"][key.lower()] = m2.group(2).strip()

    # Extract overall band
    m = re.search(r"Overall Band:\s*([0-9.]+)", raw)
    if m:
        result["overall_band"] = float(m.group(1))

    # Map score keys to short names
    score_map = {"fluency": "fluency", "vocabulary": "vocabulary", "grammar": "grammar", "pronunciation": "pronunciation", "task_achievement": "task_achievement"}
    result["scores_short"] = {}
    for long_k, short_k in score_map.items():
        if long_k in result["scores"]:
            result["scores_short"][short_k] = result["scores"][long_k]

    # Extract analysis text per criterion
    for key, label in [("FLUENCY", "fluency"), ("VOCABULARY", "vocabulary"), ("GRAMMAR", "grammar"), ("PRONUNCIATION", "pronunciation"), ("TASK_ACHIEVEMENT", "task_achievement")]:
        m = re.search(r"---" + key + r"---.*?Analysis:\s*(.+?)(?=---|\Z)", raw, re.DOTALL | re.IGNORECASE)
        if m:
            result["analyses"][label] = m.group(1).strip()

    # Extract recommendations
    m = re.search(r"---RECOMMENDATIONS---\s*(.+?)(?=---|\Z)", raw, re.DOTALL | re.IGNORECASE)
    if m:
        recs_text = m.group(1).strip()
        result["recommendations"] = [r.strip() for r in recs_text.split("\n") if r.strip() and len(r.strip()) > 5]

    return result


class CorrectionReport(FPDF):
    """PDF report for detailed IELTS speaking correction."""

    def __init__(self):
        super().__init__()
        _fd = r"C:\Windows\Fonts"
        _r = os.path.join(_fd, "msyh.ttc")
        _rb = os.path.join(_fd, "msyhbd.ttc")
        _ri = os.path.join(_fd, "msyh.ttc")
        if os.path.exists(_r):
            self.add_font("Segoe", "", _r, uni=True)
            self.add_font("Segoe", "B", _rb if os.path.exists(_rb) else _r, uni=True)
            self.add_font("Segoe", "I", _ri if os.path.exists(_ri) else _r, uni=True)

    def header(self):
        self.set_font("Segoe", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "IELTS Speaking Coach - Detailed Correction Report (AI-Assisted)", 0, 1, "C")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Segoe", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")

    def section_title(self, title):
        self.set_font("Segoe", "B", 13)
        self.set_text_color(26, 115, 232)
        self.cell(0, 10, title, 0, 1, "L")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def sub_title(self, title):
        self.set_font("Segoe", "B", 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, title, 0, 1, "L")
        self.ln(1)

    def body_text(self, text, size=10):
        self.set_font("Segoe", "", size)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, _clean_text(text))
        self.ln(2)

    def bold_text(self, text, size=10):
        self.set_font("Segoe", "B", size)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, _clean_text(text))
        self.ln(1)

    def add_score_table(self, scores_dict):
        col_w = [50, 25, 25, 90]
        headers = ["Criterion", "Score", "Target", "Status"]
        self.set_font("Segoe", "B", 9)
        self.set_fill_color(26, 115, 232)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_w[i], 7, h, 1, 0, "C", True)
        self.ln()
        self.set_font("Segoe", "", 9)
        for key, name in CRITERION_NAMES.items():
            score = scores_dict.get(key, 0)
            is_pass = score >= 7
            if score >= 7:
                status = "Meets target"
            elif score >= 5:
                status = "Needs work"
            else:
                status = "Weak"
            self.set_text_color(30, 30, 30)
            self.cell(col_w[0], 7, name, 1, 0, "L")
            self.cell(col_w[1], 7, f"{score:.1f}/9", 1, 0, "C")
            self.cell(col_w[2], 7, "7.0/9", 1, 0, "C")
            if is_pass:
                self.set_text_color(30, 180, 55)
            elif score < 5:
                self.set_text_color(200, 50, 50)
            else:
                self.set_text_color(200, 150, 30)
            self.cell(col_w[3], 7, status, 1, 0, "C")
            self.ln()
        self.ln(4)


def generate_correction_report(part, question_info, user_response, book="IELTS", test="Practice", qidx=0, topic=""):
    """Generate a detailed PDF correction report using LLM analysis."""
    save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "corrections")
    os.makedirs(save_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(save_dir, f"correction_{ts}.pdf")

    pdf = CorrectionReport()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # === TITLE ===
    pdf.set_font("Segoe", "B", 20)
    pdf.set_text_color(26, 115, 232)
    pdf.cell(0, 14, "IELTS Speaking", 0, 1, "C")
    pdf.set_font("Segoe", "", 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, "Detailed Correction Report (AI-Assisted)", 0, 1, "C")
    pdf.ln(5)

    # === TEST INFO ===
    pdf.section_title("Test Information")
    pdf.body_text(f"Test: {book} - {test}")
    pdf.body_text(f"Part: Part {part}")
    pdf.body_text(f"Question: Q{qidx+1}")
    pdf.body_text(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # === USER RESPONSE ===
    pdf.section_title("Your Response")
    pdf.body_text(user_response if user_response else "[No response provided]")

    # === LLM ANALYSIS (with loading indicator via status message) ===
    pdf.set_font("Segoe", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Analyzing response with AI examiner...", 0, 1)
    pdf.ln(3)

    raw, error = _llm_analyze_response(part, question_info, user_response, topic)
    analysis = _parse_llm_response(raw) if raw else {}

    if error:
        pdf.set_font("Segoe", "", 10)
        pdf.set_text_color(200, 50, 50)
        pdf.multi_cell(0, 6, "Note: AI analysis unavailable. " + error)
        pdf.ln(5)
        # Fallback to basic info only
        pdf.body_text("Please check your API configuration and try again.")
        pdf.output(filepath)
        return filepath

    overall = analysis.get("overall_band", 0)

    # === OVERALL SCORE ===
    pdf.section_title(f"Overall Band: {overall:.1f} / 9.0")
    if overall >= 7.0:
        pdf.set_text_color(30, 180, 55)
        pdf.body_text("PASSED - Meets the target of Band 7.0!", 12)
    else:
        pdf.set_text_color(200, 50, 50)
        pdf.body_text(f"Below target. Score: {overall:.1f}", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.ln(2)

    # === SCORE TABLE ===
    pdf.section_title("Score Breakdown")
    pdf.add_score_table(analysis.get("scores_short", {}))

    # === PER-CRITERION ANALYSIS ===
    pdf.section_title("Detailed Analysis by Criterion")

    for key, name in CRITERION_NAMES.items():
        score = analysis.get("scores_short", {}).get(key, 0)
        analysis_text = analysis.get("analyses", {}).get(key, "")
        band_int = max(1, min(9, round(score)))

        pdf.sub_title(f"{name}  --  Score: {score:.1f}/9")

        # Score bar
        if score > 0:
            pdf.set_fill_color(26, 115, 232)
            bar_w = (min(score, 9) / 9.0) * 170
            pdf.set_font("Segoe", "", 8)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(30, 5, f"Band {score:.1f}: ", 0, 0)
            pdf.cell(bar_w, 5, "", 1, 0, "", True)
            pdf.cell(0, 5, "", 0, 1)
            # Target marker
            target_bar = (7.0 / 9.0) * 170
            pdf.set_font("Segoe", "", 8)
            pdf.set_text_color(200, 100, 30)
            pdf.cell(30, 4, "Target 7.0:", 0, 0)
            pdf.cell(target_bar, 4, "", 1, 0, "", True)
            pdf.ln(5)

        if analysis_text:
            pdf.bold_text("Analysis:", 10)
            pdf.body_text(analysis_text, 9)

        # Reference descriptor
        if band_int in BAND_DESCRIPTORS_REF.get(key, {}):
            pdf.set_font("Segoe", "I", 8)
            pdf.set_text_color(100, 100, 100)
            pdf.multi_cell(0, 4.5, "Band " + str(band_int) + " reference: " + BAND_DESCRIPTORS_REF[key][band_int])
            pdf.set_text_color(30, 30, 30)

        pdf.ln(2)

    # === RECOMMENDATIONS ===
    pdf.section_title("Recommendations")
    recs = analysis.get("recommendations", [])
    if recs:
        for r in recs:
            pdf.body_text(r, 9)
    else:
        pdf.body_text("Continue practicing regularly to improve your IELTS speaking performance.", 9)

    pdf.ln(5)
    pdf.set_font("Segoe", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 6, "Generated by IELTS Speaking Coach with AI-assisted analysis (Deepseek).", 0, 1, "C")
    pdf.cell(0, 6, "Reference: Official IELTS Speaking Band Descriptors (ielts.org).", 0, 1, "C")

    pdf.output(filepath)
    return filepath


def llm_evaluate_response(part, question_info, user_response, topic=""):
    """Call LLM to evaluate a response. Returns (evaluation_dict, feedback_text).
    evaluation_dict has keys: overall_band, scores, details, word_count,
    estimated_duration_seconds, meets_duration_requirement
    """
    raw, error = _llm_analyze_response(part, question_info, user_response, topic)
    if error or not raw:
        return None, error or "LLM analysis failed"

    analysis = _parse_llm_response(raw)

    # Build scores dict
    scores = analysis.get("scores_short", {})
    
    # Create details dict with analysis text
    details = {}
    for key in ["fluency", "vocabulary", "grammar", "pronunciation", "task_achievement"]:
        details[key] = analysis.get("analyses", {}).get(key, "")

    overall = analysis.get("overall_band", 0)
    word_count = len(user_response.split()) if user_response else 0
    # Estimate duration (140 wpm)
    estimated_dur = int(word_count / 140 * 60) if word_count > 0 else 0
    # Duration check by part
    if part == 1:
        meets_dur = estimated_dur >= 25
    elif part == 2:
        meets_dur = estimated_dur >= 60
    else:
        meets_dur = estimated_dur >= 30

    # Build detailed feedback text from LLM analysis + scores
    # Similar format to scorer.generate_feedback()
    fb_lines = []
    fb_lines.append(f"OVERALL Band: {overall:.1f} / 9.0")
    if overall >= 7:
        fb_lines.append("Status: PASS (Meets Band 7.0 target)")
    else:
        fb_lines.append(f"Status: NEEDS IMPROVEMENT (target: 7.0)")
    
    criterion_names = {
        "fluency": "Fluency & Coherence",
        "vocabulary": "Lexical Resource",
        "grammar": "Grammatical Range",
        "pronunciation": "Pronunciation",
        "task_achievement": "Task Achievement"
    }
    fb_lines.append(f"\nScores:")
    for key, name in criterion_names.items():
        score = scores.get(key, 0)
        detail = details.get(key, "")[:80]
        fb_lines.append(f"  {name}: {score}/9 - {detail}")
    
    fb_lines.append(f"\nDuration: {estimated_dur}s - {'Meets target' if meets_dur else 'Below target'}")
    
    # Add recommendations
    recs = analysis.get("recommendations", [])
    if recs:
        fb_lines.append(f"\nRecommendations:")
        for i, r in enumerate(recs[:3], 1):
            fb_lines.append(f"  {i}. {r}")
    
    feedback_text = "\n".join(fb_lines)

    # Build evaluation dict compatible with scorer format
    eval_dict = {
        "overall_band": overall,
        "scores": scores,
        "details": details,
        "word_count": word_count,
        "estimated_duration_seconds": estimated_dur,
        "meets_duration_requirement": meets_dur,
        "passed": overall >= 7.0,
        "feedback_text": feedback_text,
    }
    return eval_dict, None


