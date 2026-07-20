with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", "r", encoding="utf-8") as f:
    s = f.read()

old = '''        return {
            "overall_band": overall,
            "scores": scores,
            "details": {'''

new = '''        # Safety: ensure minimum score of 3 for any criterion
        for k in scores:
            scores[k] = max(3.0, scores[k])
        return {
            "overall_band": overall,
            "scores": scores,
            "details": {'''

s = s.replace(old, new)

with open(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", "w", encoding="utf-8") as f:
    f.write(s)

import py_compile
py_compile.compile(r"D:\EricWork\IELTS-SpeakingCoach\engine\scorer.py", doraise=True)
print("Scorer safeguard - OK")
