def evaluate_user_message(content: str) -> dict:
    length_score = min(5, max(0, len(content.split()) // 8))
    rubric_scores = {
        "clarity": length_score,
        "specificity": max(1, min(5, 5 if any(ch.isdigit() for ch in content) else 2)),
        "consistency": 3,
        "responsibility": 3,
    }
    feedback = "Good effort. Add concrete examples and timelines for stronger MPU answers."
    return {
        "rubric_scores": rubric_scores,
        "summary_feedback": feedback,
        "detected_issues": {"contradictions": []},
    }
