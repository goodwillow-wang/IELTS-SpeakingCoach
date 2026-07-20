import os, re

# ========== 1) Add llm_evaluate_response() to correction_report.py ==========
with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c = f.read()

# Find insertion point: after generate_correction_report function, before the end of file
# Add a new function for LLM-based evaluation
new_fn = '''

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
    fb_lines.append(f"\\nScores:")
    for key, name in criterion_names.items():
        score = scores.get(key, 0)
        detail = details.get(key, "")[:80]
        fb_lines.append(f"  {name}: {score}/9 - {detail}")
    
    fb_lines.append(f"\\nDuration: {estimated_dur}s - {'Meets target' if meets_dur else 'Below target'}")
    
    # Add recommendations
    recs = analysis.get("recommendations", [])
    if recs:
        fb_lines.append(f"\\nRecommendations:")
        for i, r in enumerate(recs[:3], 1):
            fb_lines.append(f"  {i}. {r}")
    
    feedback_text = "\\n".join(fb_lines)

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


'''

# Insert before the last line (which is empty or has nothing)
# Find the generate_correction_report function end
idx = c.rfind("def generate_correction_report")
if idx > 0:
    # Find the end of this function (the file ends after it)
    # Replace the last occurrence of the file end pattern
    c = c + new_fn
    print("Added llm_evaluate_response function")
else:
    print("ERROR: generate_correction_report not found")

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "w", encoding="utf-8") as f:
    f.write(c)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", doraise=True)
print("Syntax OK")


# ========== 2) Update submit() in main.py ==========
with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    m = f.read()

# Add import for llm_evaluate_response
old_import = "from engine.correction_report import generate_correction_report"
new_import = "from engine.correction_report import generate_correction_report, llm_evaluate_response"
m = m.replace(old_import, new_import)
print("Import updated: OK")

# Modify submit() to use LLM instead of local scorer
# Find the scorer call and replace with LLM call
old_submit = '''        self.attempts += 1
        d = self.qdata
        pi = 1
        if "questions" in d:
            q = d["questions"][self.qidx]
            qt = q.get("type", "P2")
            pi = int(qt[1]) if len(qt) >= 2 else 2
            if qt == "P2":
                qi = q
            else:
                qi = [q.get('question','')]
        elif self.part == "Part 2 - Individual Long Turn":
            pi = 2
            cue_cards = d.get("cue_cards", None)
            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):
                qi = cue_cards[self.qidx]
            else:
                qi = d
        else:
            pi = self.pc.currentIndex() + 1 if hasattr(self, 'pc') else 1
            qs = d.get("questions", [])
            qi = [qs[self.qidx]] if self.qidx < len(qs) else qs
        
        ev = self.scorer.evaluate_full_response(text, qi, pi)
        self.eval = ev
        self.fa.setText(self.scorer.generate_feedback(ev))'''

new_submit = '''        self.attempts += 1
        d = self.qdata
        pi = 1
        qi = None
        if "questions" in d:
            q = d["questions"][self.qidx]
            qt = q.get("type", "P2")
            pi = int(qt[1]) if len(qt) >= 2 else 2
            qi = q
        elif self.part == "Part 2 - Individual Long Turn":
            pi = 2
            cue_cards = d.get("cue_cards", None)
            if cue_cards and isinstance(cue_cards, list) and self.qidx < len(cue_cards):
                qi = cue_cards[self.qidx]
            else:
                qi = d
        else:
            pi = self.pc.currentIndex() + 1 if hasattr(self, 'pc') else 1
            qs = d.get("questions", [])
            qi = [qs[self.qidx]] if self.qidx < len(qs) else qs
        
        # Try LLM-based evaluation first
        self.fa.setText("Analyzing with AI examiner...")
        self.bs.setText("AI analyzing your response...")
        self.bs.repaint()
        import time as _t
        _t.sleep(0.1)  # Allow UI update
        
        from engine.correction_report import llm_evaluate_response
        llm_ev, llm_err = llm_evaluate_response(pi, qi, text, self.current_topic)
        
        if llm_ev and not llm_err:
            ev = llm_ev
            self.eval = llm_ev
            self.fa.setText(llm_ev.get("feedback_text", ""))
        else:
            # Fallback to local scorer
            self.bs.setText("AI analysis unavailable, using local evaluation...")
            ev = self.scorer.evaluate_full_response(text, qi, pi)
            self.eval = ev
            self.fa.setText(self.scorer.generate_feedback(ev))
        
        band = ev.get("overall_band", 0)'''

m = m.replace(old_submit, new_submit)
print("submit() updated: OK")

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(m)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\main.py", doraise=True)
print("main.py syntax: OK")
print("\\nALL DONE")
