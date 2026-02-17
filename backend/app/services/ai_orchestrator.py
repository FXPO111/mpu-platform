from sqlalchemy.orm import Session

from app.db.repo import Repo
from app.integrations.llm_openai import generate_assistant_reply
from app.services.question_bank import next_question
from app.services.scoring import evaluate_user_message


def process_user_message(db: Session, session_id, user_content: str, locale: str, mode: str):
    repo = Repo(db)
    user_msg = repo.add_message(session_id, "user", user_content)
    scoring = evaluate_user_message(user_content)
    question = next_question(db, locale=locale)
    assistant_content = generate_assistant_reply(mode=mode, question=question, user_answer=user_content, locale=locale)
    assistant_msg = repo.add_message(session_id, "assistant", assistant_content)
    repo.add_evaluation(
        session_id=session_id,
        message_id=user_msg.id,
        rubric_scores=scoring["rubric_scores"],
        summary_feedback=scoring["summary_feedback"],
        detected_issues=scoring["detected_issues"],
    )
    return assistant_msg
