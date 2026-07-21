import re
p = r"D:\EricWork\IELTS-SpeakingCoach\main.py"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

# The problem: in show_q(), "questions" in d is True for BOTH custom flat format AND standard part dicts
# Custom flat: {"questions": [{"type": "P1", ...}, ...]}
# Standard part: {"topic": "Games", "questions": ["Q1", "Q2", ...]}
# Fix: skip the custom branch when it has "topic" or "cue_card"

old = '        if "questions" in d:'
new = '        if "questions" in d and "topic" not in d and "cue_card" not in d:'
c = c.replace(old, new)

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed!")
