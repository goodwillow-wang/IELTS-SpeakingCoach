with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c = f.read()

# Replace Segoe UI font with Microsoft YaHei (supports Chinese)
old_font = r"C:\Windows\Fonts\segoeui.ttf"
new_font = r"C:\Windows\Fonts\msyh.ttc"
c = c.replace(old_font, new_font)

old_font_b = r"C:\Windows\Fonts\segoeuib.ttf"
new_font_b = r"C:\Windows\Fonts\msyhbd.ttc"  # Microsoft YaHei Bold
c = c.replace(old_font_b, new_font_b)

old_font_i = r"C:\Windows\Fonts\segoeuii.ttf"
# For italic, use the same regular font since YaHei doesn't have italic
new_font_i = r"C:\Windows\Fonts\msyh.ttc"
c = c.replace(old_font_i, new_font_i)

# Also update font family name references from "Segoe" to "YaHei"
# But keep the family name as "Segoe" so we don't need to change all the set_font calls
# Actually, the family name registered in add_font is the first argument
# Let me check: the code uses "Segoe" as family name
# If I keep the family name as "Segoe" but point to msyh.ttc, it should work

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "w", encoding="utf-8") as f:
    f.write(c)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", doraise=True)
print("Updated to Microsoft YaHei - OK")
