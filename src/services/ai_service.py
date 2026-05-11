from google import genai
from src.core.config import settings


def ask_gemini(prompt: str) -> str | None:
    client = genai.Client(api_key=settings.gemini_api_key.get_secret_value())
    chat = client.chats.create(model="gemini-2.5-flash")

    try:
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Ошибка AI-модуля: {str(e)}")
        return None
