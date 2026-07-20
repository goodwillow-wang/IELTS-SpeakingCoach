import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"D:\EricWork\IELTS-SpeakingCoach")
from engine.correction_report import generate_correction_report

eval_data = {
    "overall_band": 5.5,
    "scores": {"fluency": 5, "vocabulary": 6, "grammar": 5, "pronunciation": 6, "task_achievement": 5},
    "details": {"fluency": "Short response (45 words) with 2 connectives", "vocabulary": "Basic vocabulary, some repetition", "grammar": "Mostly simple sentences with some errors", "pronunciation": "Limited sentence variety", "task_achievement": "Addressed 2 of 4 prompts"},
    "estimated_duration_seconds": 22,
    "meets_duration_requirement": False,
    "word_count": 45
}

fp = generate_correction_report(eval_data, {"cue_card": "Describe a person", "prompts": ["Who", "What", "Why"]}, "I have a friend. His name is Tom. He is very kind. I like him because he helps me.", part=2, book="Cambridge 9", test="Test 1", qidx=0)
print(f"PDF generated: {fp}")
print(f"File size: {os.path.getsize(fp)} bytes")
