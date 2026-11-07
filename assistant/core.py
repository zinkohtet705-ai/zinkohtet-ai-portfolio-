from assistant.client import ask_model

def respond(message: str) -> str:
    """Respond using the optional OpenAI integration, with a safe fallback."""
    cleaned = message.strip()
    if not cleaned:
        return "Please enter a message."
    try:
        answer = ask_model(cleaned)
        if answer:
            return answer
    except Exception as exc:
        return f"AI service error: {exc}"
    return (
        "The local assistant is running, but AI integration is not configured. "
        "Add OPENAI_API_KEY to your local .env file to enable it."
    )
