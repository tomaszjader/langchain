from google_adk import LlmAgent

from config import load_config, validate_google_key
from tools import get_current_time_plain, calculator_plain


def run_adk_agent():
    """Uruchamia agenta ADK z narzędziami: czas i kalkulator."""
    load_config()

    if not validate_google_key():
        return

    # Inicjalizacja agenta ADK
    agent = LlmAgent(
        name="helpful_assistant",
        model="gemini-1.5-flash",
        instruction="You are a helpful assistant. You have access to tools. Use them to answer the user's question.",
        tools=[get_current_time_plain, calculator_plain]
    )

    # Przykładowe zapytanie wymagające obu narzędzi
    query = "Która jest teraz godzina i ile to jest 123 razy 4?"
    print(f"\n--- Query: {query} ---\n")

    try:
        response = agent.run(query)
        print(f"\n--- Agent Response: ---\n{response}")
    except Exception as e:
        print(f"\n--- Error running agent: ---\n{e}")


if __name__ == "__main__":
    run_adk_agent()
