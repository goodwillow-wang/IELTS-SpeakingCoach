import re

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Add font registration in CorrectionReport.__init__
# The current class doesn't have __init__, so we add one
old_start = 'class CorrectionReport(FPDF):\n    """PDF report for detailed IELTS speaking correction."""\n\n    def header(self):'
new_start = '''class CorrectionReport(FPDF):
    """PDF report for detailed IELTS speaking correction."""
    def __init__(self):
        super().__init__()
        # Register Unicode fonts from Windows
        import os as _os
        _fd = r"C:\\Windows\\Fonts"
        _r = _os.path.join(_fd, "segoeui.ttf")
        _rb = _os.path.join(_fd, "segoeuib.ttf")
        _ri = _os.path.join(_fd, "segoeuii.ttf")
        if _os.path.exists(_r):
            self.add_font("Segoe", "", _r, uni=True)
            self.add_font("Segoe", "B", _rb if _os.path.exists(_rb) else _r, uni=True)
            self.add_font("Segoe", "I", _ri if _os.path.exists(_ri) else _r, uni=True)

    def header(self):'''

c = c.replace(old_start, new_start)

# 2) Replace all Helvetica font references with Segoe
c = c.replace('"Helvetica"', '"Segoe"')
c = c.replace("self.set_font(\"Helvetica\"", 'self.set_font("Segoe"')

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated to Segoe UI font")

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", doraise=True)
print("Syntax OK")
