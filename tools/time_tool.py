from datetime import datetime
from langchain_core.tools import tool


@tool
def get_current_time():
    """Zwraca aktualny czas w formacie HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")


def get_current_time_plain():
    """Zwraca aktualny czas (wersja bez dekoratora LangChain, dla ADK)."""
    return datetime.now().strftime("%H:%M:%S")
