def generate_assistant_reply(mode: str, question: str, user_answer: str, locale: str) -> str:
    if locale == "de":
        return f"Danke. {question} Bitte werden Sie konkreter zu Verantwortung und Lernfortschritt."
    return f"Thanks. {question} Please be more specific about responsibility and what changed."
