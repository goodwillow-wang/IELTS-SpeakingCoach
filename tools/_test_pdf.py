import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"D:\EricWork\IELTS-SpeakingCoach")
from engine.correction_report import generate_correction_report

eval_data = {
    "overall_band": 5.5,
    "scores": {"fluency": 5, "vocabulary": 6, "grammar": 5, "pronunciation": 6, "task_achievement": 5},
    "details": {"fluency": "Short response with filler words", "vocabulary": "Basic vocab", "grammar": "Simple sentences", "pronunciation": "Limited", "task_achievement": "Partial"},
    "estimated_duration_seconds": 22,
    "meets_duration_requirement": False,
    "word_count": 45
}

# Test with feedback containing emoji characters
fp = generate_correction_report(eval_data, {"cue_card": "Describe a person"}, 
    "My test response with emoji \u2705 check and \u274c cross.", 
    part=2, book="Cambridge 9", test="Test 1", qidx=0)
print(f"PDF generated: {fp}")
print(f"Size: {os.path.getsize(fp)} bytes")
os.remove(fp)
print("Cleanup OK")
