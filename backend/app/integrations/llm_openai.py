from __future__ import annotations

import os

from app.settings import settings

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def _fallback(mode: str, question: str, locale: str) -> str:
    if (locale or "de").strip().lower().startswith("de"):
        return (
            "Feedback: Bitte antworten Sie konkreter (Fakten, Zeitpunkte, Ihr Anteil).\n\n"
            f"Nächste Frage: {question}"
        )
    return (
        "Feedback: Please be more concrete (facts, dates, your responsibility).\n\n"
        f"Next question: {question}"
    )


def generate_assistant_reply(mode: str, question: str, user_answer: str, locale: str) -> str:
    """
    Generates assistant reply for MPU training.
    Output contract:
      - short feedback on user's last answer (clarity/responsibility/specificity/consistency)
      - then asks the provided `question` as the next question
    """
    if not getattr(settings, "openai_api_key", None):
        return _fallback(mode=mode, question=question, locale=locale)

    loc = (locale or "de").strip().lower()
    is_de = loc.startswith("de")

    if is_de:
        system = (
            "Du bist ein strenger MPU-Interviewtrainer. "
            "Deine Aufgabe: kurze, konkrete Rückmeldung geben und dann die nächste Frage stellen. "
            "Keine langen Erklärungen, keine Floskeln. Keine erfundenen Fakten.\n"
            "Format:\n"
            "Feedback: 2-4 Sätze (Klarheit, Verantwortung, Konkretheit, evtl. Widerspruch).\n"
            "Nächste Frage: <genau eine Frage>\n"
        )
        user = (
            f"Modus: {mode}\n"
            f"Letzte Antwort des Nutzers:\n{user_answer}\n\n"
            f"Bitte stelle als nächste Frage exakt diese:\n{question}\n"
        )
    else:
        system = (
            "You are a strict MPU interview trainer. "
            "Your job: give short, concrete feedback, then ask the next question. "
            "No long explanations, no fluff. Do not invent facts.\n"
            "Format:\n"
            "Feedback: 2-4 sentences (clarity, responsibility, specificity, contradictions if any).\n"
            "Next question: <exactly one question>\n"
        )
        user = (
            f"Mode: {mode}\n"
            f"User's last answer:\n{user_answer}\n\n"
            f"Ask exactly this as the next question:\n{question}\n"
        )

    model = getattr(settings, "openai_model", None) or DEFAULT_MODEL

    # 1) Try Responses API (new)
    try:
        from openai import OpenAI  # type: ignore

        client = OpenAI(api_key=settings.openai_api_key)

        resp = client.responses.create(
            model=model,
            instructions=system,
            input=user,
        )

        text = getattr(resp, "output_text", None)
        if text and str(text).strip():
            return str(text).strip()

        # fallback: try to extract from structured output
        try:
            out: list[str] = []
            for item in getattr(resp, "output", []) or []:
                if getattr(item, "type", None) == "message":
                    for c in getattr(item, "content", []) or []:
                        if getattr(c, "type", None) in ("output_text", "text"):
                            out.append(getattr(c, "text", "") or "")
            joined = "\n".join([t for t in out if t]).strip()
            if joined:
                return joined
        except Exception:
            pass

        return _fallback(mode=mode, question=question, locale=locale)

    except Exception:
        pass

    # 2) Fallback to Chat Completions (older envs)
    try:
        from openai import OpenAI  # type: ignore

        client = OpenAI(api_key=settings.openai_api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        content = resp.choices[0].message.content
        if content and content.strip():
            return content.strip()
    except Exception:
        pass

    return _fallback(mode=mode, question=question, locale=locale)
