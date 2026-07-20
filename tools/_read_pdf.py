import pdfplumber, sys

sys.stdout.reconfigure(encoding="utf-8")

path = r"D:\EricWork\IELTS-AuthenticTest\SpeakingBandDescriptors\ielts_speaking_key_assessment_criteria.pdf"
with pdfplumber.open(path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f"=== PAGE {i+1} ===")
            print(text[:3000])
            print()
