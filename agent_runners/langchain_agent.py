from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from config import load_config, validate_openai_key
from tools import get_current_time, calculator, get_weather


def run_langchain_agent():
    """Uruchamia agenta LangChain z narzędziami: czas i kalkulator."""
    load_config()

    if not validate_openai_key():
        return

    # Inicjalizacja modelu językowego
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Lista dostępnych narzędzi
    tools = [get_current_time, calculator, get_weather]

    # Tworzenie agenta (LangChain 1.0 / LangGraph)
    agent = create_react_agent(
        llm,
        tools,
        prompt="Jesteś pomocnym asystentem. Użyj narzędzi, aby odpowiedzieć na pytanie użytkownika.",
    )

    # Przykładowe zapytanie wymagające obu narzędzi
    query = "Która jest teraz godzina i ile to jest 123 razy 4?"
    print(f"\n--- Zapytanie: {query} ---\n")

    response = agent.invoke({"messages": [("human", query)]})

    # Wyciągnięcie ostatniej odpowiedzi
    last_message = response["messages"][-1]
    print(f"\n--- Odpowiedź agenta: ---\n{last_message.content}")


if __name__ == "__main__":
    run_langchain_agent()
