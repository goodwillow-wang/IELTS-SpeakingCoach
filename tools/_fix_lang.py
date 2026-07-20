with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c = f.read()

# 1) System prompt: add Chinese instruction
old1 = "Return your analysis in the EXACT structured format below, with each section clearly marked."
new1 = "Write all Analysis sections in Chinese. Official Level descriptions keep in English. Return your analysis in the EXACT structured format below."
c = c.replace(old1, new1)

# 2) Format instructions: add "(in Chinese)" to Analysis fields
old2 = "Analysis: [2-3 sentences analyzing the response]"
new2 = "Analysis: [2-3 sentences in Chinese, analyzing the response]"
c = c.replace(old2, new2)

old3 = "Analysis: [2-3 sentences]"
new3 = "Analysis: [2-3 sentences in Chinese]"
c = c.replace(old3, new3)

# 3) Update important note
old4 = "IMPORTANT: Be honest and accurate. Use ONLY the EXACT section headers shown above."
new4 = "IMPORTANT: Write Analysis sections in Chinese. Official Level in English. Be accurate. Use ONLY the EXACT section headers shown above."
c = c.replace(old4, new4)

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "w", encoding="utf-8") as f:
    f.write(c)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", doraise=True)
print("Chinese analysis - OK")
