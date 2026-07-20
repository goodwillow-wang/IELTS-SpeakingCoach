with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c = f.read()

old_r = '_r = os.path.join(_fd, "segoeui.ttf")'
new_r = '_r = os.path.join(_fd, "msyh.ttc")'
c = c.replace(old_r, new_r)

old_rb = '_rb = os.path.join(_fd, "segoeuib.ttf")'
new_rb = '_rb = os.path.join(_fd, "msyhbd.ttc")'
c = c.replace(old_rb, new_rb)

old_ri = '_ri = os.path.join(_fd, "segoeuii.ttf")'
new_ri = '_ri = os.path.join(_fd, "msyh.ttc")'
c = c.replace(old_ri, new_ri)

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "w", encoding="utf-8") as f:
    f.write(c)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", doraise=True)

# Verify
with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\correction_report.py", "r", encoding="utf-8") as f:
    c2 = f.read()
if "msyh.ttc" in c2 and "segoeui.ttf" not in c2:
    print("Font paths updated to msyh.ttc - OK")
else:
    print("ERROR: font paths not updated")
