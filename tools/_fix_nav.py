with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "r", encoding="utf-8") as f:
    m = f.read()

# Remove max width constraint on nav buttons - let them auto-size
old1 = '        self.prev_q_btn = QPushButton("< Prev")\n        self.prev_q_btn.setMaximumWidth(80)'
new1 = '        self.prev_q_btn = QPushButton("< Prev")'
m = m.replace(old1, new1)

old2 = '        self.next_q_btn = QPushButton("Next >")\n        self.next_q_btn.setMaximumWidth(80)'
new2 = '        self.next_q_btn = QPushButton("Next >")'
m = m.replace(old2, new2)

with open(r"D:\EricWork\IELTS-SpeakingCoach\main.py", "w", encoding="utf-8") as f:
    f.write(m)
print("Fixed button widths")
