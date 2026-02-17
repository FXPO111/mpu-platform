from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.integrations.llm_openai import generate_assistant_reply
from app.services.question_bank import next_question
from app.services.scoring import evaluate_user_message


def process_user_message(db: Session, session_id, user_content: str, locale: str, mode: str):
    """
    - writes user message
    - evaluates it (rubrics)
    - picks next question (mode-aware)
    - generates assistant reply via LLM
    - writes assistant message
    - stores evaluation linked to the user message
    """
    repo = Repo(db)

    content = (user_content or "").strip()
    if not content:
        # service-level guard; routes should also validate
        raise ValueError("Empty user message")

    user_msg = repo.add_message(session_id, "user", content)

    scoring = evaluate_user_message(content)

    # IMPORTANT: mode-aware question selection
    mode_norm = (mode or "").strip().lower() or None
    question = next_question(db, locale=locale, mode=mode_norm)

    assistant_content = generate_assistant_reply(
        mode=mode_norm or "practice",
        question=question,
        user_answer=content,
        locale=locale,
    )
    assistant_msg = repo.add_message(session_id, "assistant", assistant_content)

    repo.add_evaluation(
        session_id=session_id,
        message_id=user_msg.id,
        rubric_scores=scoring.get("rubric_scores", {}),
        summary_feedback=scoring.get("summary_feedback", ""),
        detected_issues=scoring.get("detected_issues", {}),
    )
    return assistant_msg
