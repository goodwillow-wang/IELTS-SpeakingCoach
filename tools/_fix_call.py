with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    m = f.read()

old = '''            filepath = generate_correction_report(
                self.eval,
                self.last_question_info,
                self.last_user_response,
                self.current_part_num,
                self.book or "IELTS",
                self.test or "Practice",
                self.qidx
            )'''

new = '''            filepath = generate_correction_report(
                self.current_part_num,
                self.last_question_info,
                self.last_user_response,
                book=self.book or "IELTS",
                test=self.test or "Practice",
                qidx=self.qidx,
                topic=self.current_topic
            )'''

m = m.replace(old, new)

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(m)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\main.py", doraise=True)
print("Call signature updated - OK")
