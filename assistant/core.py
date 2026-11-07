def respond(message: str) -> str:
    """Return a safe placeholder response.

    Future model and tool integrations must be explicit opt-ins.
    """
    if not message.strip():
        return "Please enter a message."
    return (
        "I received your message. The local assistant starter is running; "
        "external model and tool integrations are not enabled yet."
    )
