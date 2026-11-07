import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def ask_model(message: str) -> str | None:
    """Call the OpenAI Responses API when a local API key is configured."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
        input=message,
    )
    return response.output_text.strip()
