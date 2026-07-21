# Fix the generation script comma logic
import re
with open(r"D:\EricWork\IELTS-SpeakingCoach\tools\generate_v3.py", "r", encoding="utf-8") as f:
    c = f.read()

old = '    output[-1] += ","'
new = '    if not output[-1].rstrip().endswith(","):\n        output[-1] += ","'
c = c.replace(old, new)

with open(r"D:\EricWork\IELTS-SpeakingCoach\tools\generate_v3.py", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed!")

# Re-run to regenerate clean file
exec(compile(open(r"D:\EricWork\IELTS-SpeakingCoach\tools\generate_v3.py").read(), "generate_v3.py", "exec"))
