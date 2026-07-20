with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    c = f.read()

old = '        dlg.exec_()\n    \n    def retry(self):'

method_code = '''        dlg.exec_()
    
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

c = c.replace(old, method_code)

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(c)

print("Method inserted")
