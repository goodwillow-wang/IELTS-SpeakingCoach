import re, os

path = r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1) Add _clean_text function before CorrectionReport class
old = "class CorrectionReport(FPDF):"
new_cleaner = '''import re as _re

def _clean_text(text):
    """Remove or replace characters not suitable for PDF fonts."""
    if not text:
        return text
    repl = {
        "\\u2705": "[PASS] ",
        "\\u274c": "[FAIL] ",
        "\\u26a0\\ufe0f": "[WARN] ",
        "\\ufe0f": "",
        "\\u2605": "*",
    }
    for ch, r in repl.items():
        text = text.replace(ch, r)
    # Remove remaining non-BMP characters
    out = []
    for ch in text:
        if ord(ch) < 0x10000:
            out.append(ch)
    return "".join(out)

''' + old

c = c.replace(old, new_cleaner, 1)

# 2) Apply _clean_text in body_text and bold_text methods
c = c.replace(
    "self.multi_cell(0, 5.5, text)\n        self.ln(2)",
    "self.multi_cell(0, 5.5, _clean_text(text))\n        self.ln(2)"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

import py_compile
py_compile.compile(path, doraise=True)
print("Text cleaning added - OK")
