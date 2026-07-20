import sys, os, re

# =====================
# 1) scorer.py - update band descriptors to official text
# =====================
with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", "r", encoding="utf-8") as f:
    s = f.read()

# Replace the __init__ band_descriptors with official text
old_descriptors = '''    def __init__(self):
        self.band_descriptors = {
            "fluency_coherence": {
                7: "Speaks at length without noticeable effort. Uses a range of connectives. Some hesitation, but mostly flow.",
                6: "Willing to speak at length, though may lose coherence. Uses some connectives. Repetition and hesitation.",
                5: "Usually maintains flow but uses simple connectives. Hesitation and repetition more noticeable."
            },
            "lexical_resource": {
                7: "Uses vocabulary flexibly to discuss topics. Uses some less common words. Good paraphrasing.",
                6: "Has enough vocabulary to discuss topics at some length. Some paraphrasing. Some inaccuracy.",
                5: "Manages to talk about familiar topics. Limited vocabulary. Frequent errors in word choice."
            },
            "grammatical_range": {
                7: "Uses a variety of complex structures. Frequent error-free sentences. Good control.",
                6: "Uses mix of simple and complex structures. Some errors but meaning clear.",
                5: "Uses only basic sentence forms. Frequent errors. Limited accuracy."
            },
            "pronunciation": {
                7: "Easy to understand throughout. Uses intonation and stress. Good rhythm.",
                6: "Clear enough to understand. Some mispronunciation. Some intonation.",
                5: "Can be understood but with effort. Pronunciation errors noticeable."
            },
            "task_achievement": {
                7: "Addresses all parts of the task. Presents well-developed response. Relevant detail.",
                6: "Addresses the task. Main parts covered. Some under/over development.",
                5: "Addresses task only partially. Format sometimes inappropriate."
            }
        }'''

new_descriptors = '''    def __init__(self):
        self.band_descriptors = {
            "fluency_coherence": {
                9: "Fluent with only very occasional repetition. Sustained use of accurate language. Hesitation only to prepare content.",
                8: "Fluent with only very occasional repetition. Hesitation occasionally for content. Topic development coherent and relevant.",
                7: "Keeps going and readily produces long turns. Uses a range of connectives. Some hesitation, repetition or self-correction.",
                6: "Willing to speak at length, though coherence may be lost at times. Uses discourse markers not always appropriately.",
                5: "Usually able to keep going, but relies on repetition/self-correction. Hesitations for basic lexis and grammar.",
                4: "Cannot respond without noticeable pauses. Only simple speech, frequently with repetition and hesitation.",
                3: "Frequent long pauses while searching for words. Limited ability to link sentences.",
                2: "Lengthy pauses before nearly every word. Virtually no communicative significance.",
                1: "Essentially no rateable language. Speech is totally incoherent."
            },
            "lexical_resource": {
                9: "Total flexibility and precise use in all contexts. Skilful use of idiomatic language naturally.",
                8: "Wide resource, readily and flexibly used. Skilful use of less common items despite occasional inaccuracies.",
                7: "Resource sufficient to discuss topics at length. Good paraphrasing. Uses some less common vocabulary.",
                6: "Resource sufficient for topics at some length. Generally able to paraphrase. Some inappropriacies in word choice.",
                5: "Resource sufficient for familiar topics but limited flexibility. Attempts paraphrase not always successful.",
                4: "Limited vocabulary, primarily basic. Inadequate for unfamiliar topics. Frequent word choice errors.",
                3: "Limited to simple vocabulary for personal information. Frequently unable to convey basic meaning.",
                2: "Very limited resource. Utterances are isolated words or memorised utterances.",
                1: "No resource bar a few isolated words. No communication possible."
            },
            "grammatical_range": {
                9: "Structures are precise and accurate at all times. Full range of structures used naturally.",
                8: "Wide range of structures, flexibly used. Majority of sentences error-free. Occasional non-systematic errors.",
                7: "Mix of short and complex sentence forms. Frequent error-free sentences. Good grammatical control.",
                6: "Mix of short and complex forms with limited flexibility. Errors in complex structures but rarely impede.",
                5: "Basic sentence forms fairly well controlled. Complex structures limited and nearly always contain errors.",
                4: "Basic forms attempted but numerous errors except in memorised utterances.",
                3: "No evidence of basic sentence forms except memorised. Numerous grammatical errors.",
                2: "No evidence of basic sentence forms. Delivery problems impair connected speech.",
                1: "No rateable language unless memorised."
            },
            "pronunciation": {
                9: "Full range of phonological features for precise meaning. Flexible connected speech. Effortlessly understood.",
                8: "Wide range of phonological features. Appropriate rhythm. Flexible stress/intonation. Easily understood.",
                7: "Range of phonological features, control variable. Chunking generally appropriate. Some effective intonation/stress.",
                6: "Range of features but not sustained. Chunking appropriate. Some effective intonation but limited.",
                5: "Some features of band 4 and some of band 6. Occasional mispronunciation but meaning usually clear.",
                4: "Few acceptable phonological features. Isolated words may be recognisable.",
                3: "Individual words and phonemes mainly mispronounced. Little meaning conveyed.",
                2: "Often unintelligible. Little meaning conveyed.",
                1: "Can produce occasional recognisable words but no overall meaning. Unintelligible."
            },
            "task_achievement": {
                9: "Fully addresses all parts with well-developed, relevant and extended responses.",
                8: "Addresses all parts with well-developed responses and relevant detail throughout.",
                7: "Addresses all parts of the task. Well-developed responses with relevant supporting detail.",
                6: "Addresses all parts though some may be more fully covered. Relevant but may lack detail.",
                5: "Addresses task only partially. Mainly relevant but may lack specific detail.",
                4: "Attempts task but does not address all parts. May be off-topic at times.",
                3: "Addresses task only minimally. Frequently off-topic. Very limited content.",
                2: "Hardly addresses the task. Mostly irrelevant or very brief.",
                1: "Does not address the task. Completely unrelated or insufficient."
            }
        }'''

s = s.replace(old_descriptors, new_descriptors)
print("1) scorer.py band descriptors: OK")

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", "w", encoding="utf-8") as f:
    f.write(s)

# =====================
# 2) main.py - add correction report button
# =====================
with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    m = f.read()

# 2a) Add import
if "from engine.sample_answers import" in m:
    m = m.replace("from engine.sample_answers import generate_sample_answers, save_as_docx",
                  "from engine.sample_answers import generate_sample_answers, save_as_docx\nfrom engine.correction_report import generate_correction_report")
    print("2a) Import: OK")
else:
    print("2a) Import: WARNING - import line not found")

# 2b) Add correction button in init_ui after sample_btn
old_sb = '        self.sample_btn.setVisible(False)\n        rl2.addWidget(self.sample_btn)'
new_sb = '        self.sample_btn.setVisible(False)\n        rl2.addWidget(self.sample_btn)\n        self.correction_btn = QPushButton(\"[PDF] Correction Report\")\n        self.correction_btn.setObjectName(\"s\")\n        self.correction_btn.clicked.connect(self.show_correction_report)\n        self.correction_btn.setEnabled(False)\n        self.correction_btn.setVisible(False)\n        rl2.addWidget(self.correction_btn)'
m = m.replace(old_sb, new_sb)
print("2b) Correction button: OK")

# 2c) In submit(): enable correction button (after sample_btn)
old_sb_enable = '        self.sample_btn.setEnabled(True)\n        self.sample_btn.setVisible(True)'
# Need to find this in submit() - there should be one occurrence
new_sb_enable = '        self.sample_btn.setEnabled(True)\n        self.sample_btn.setVisible(True)\n        self.correction_btn.setEnabled(True)\n        self.correction_btn.setVisible(True)'
m = m.replace(old_sb_enable, new_sb_enable)
print("2c) Submit enable correction: OK")

# 2d) In show_q(): also hide correction_btn alongside sample_btn
# The sample_btn is hidden/disabled in show_q at the start
# Find where sample buttons are disabled in show_q
old_sb_hide = '        self.sample_btn.setEnabled(False)\n        self.sample_btn.setVisible(False)'
# This appears at the start of show_q - need to add correction_btn
new_sb_hide = '        self.sample_btn.setEnabled(False)\n        self.sample_btn.setVisible(False)\n        self.correction_btn.setEnabled(False)\n        self.correction_btn.setVisible(False)'
m = m.replace(old_sb_hide, new_sb_hide)
print("2d) Show_q hide correction: OK")

# 2e) Add show_correction_report method - before save_exit (the last methods)
# Find a good insertion point: after show_sample_dialog method
old_ssd = '        save_btn.clicked.connect(on_save)\n        cancel_btn.clicked.connect(dlg.reject)\n        dlg.exec_()\n\n    def retry(self):'
# Need to find the show_sample_dialog's end and insert before retry
# Actually, let me insert the method right after show_sample_dialog's last close brace
# The show_sample_dialog method ends with dlg.exec_() and then the next method
# Let me find a better insertion point

# Insert after the show_sample_dialog method (before retry)
old_after = '        dlg.exec_()\n\n    def retry(self):'
new_after = '''        dlg.exec_()
    
    def show_correction_report(self):
        """Generate and open the detailed PDF correction report."""
        if not self.eval:
            QMessageBox.information(self, "Info", "No evaluation data. Submit a response first.")
            return
        if not self.last_user_response:
            QMessageBox.information(self, "Info", "No response to evaluate.")
            return
        try:
            filepath = generate_correction_report(
                self.eval,
                self.last_question_info,
                self.last_user_response,
                self.current_part_num,
                self.book or "IELTS",
                self.test or "Practice",
                self.qidx
            )
            import os as _os
            try:
                _os.startfile(filepath)
            except Exception:
                QMessageBox.information(self, "Saved", "Correction report saved to:\\n" + filepath)
        except Exception as ex:
            QMessageBox.warning(self, "Error", "Failed to generate report:\\n" + str(ex))
    
    def retry(self):'''

m = m.replace(old_after, new_after)
print("2e) show_correction_report method: OK")

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(m)

# =====================
# Verify syntax
# =====================
import py_compile
try:
    py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\main.py", doraise=True)
    py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", doraise=True)
    print("3) Syntax: OK")
except py_compile.PyCompileError as e:
    print(f"3) Syntax ERROR: {e}")
