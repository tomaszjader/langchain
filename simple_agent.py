import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import tool, AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Ładowanie zmiennych środowiskowych (np. OPENAI_API_KEY)
load_dotenv()

# 1. Definicja narzędzia: Aktualny czas
@tool
def get_current_time():
    """Zwraca aktualny czas w formacie HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")

# 2. Definicja narzędzia: Kalkulator
@tool
def calculator(expression: str):
    """Oblicza wynik prostego wyrażenia matematycznego. Argumentem powinno być wyrażenie, np. '2 + 2'."""
    try:
        # UWAGA: eval() jest używany tutaj dla uproszczenia przykładu. 
        # W środowisku produkcyjnym należy używać bezpieczniejszych metod (np. numexpr).
        return eval(expression)
    except Exception as e:
        return f"Błąd obliczeń: {e}"

def main():
    # Sprawdzenie czy klucz API jest dostępny
    if not os.getenv("OPENAI_API_KEY"):
        print("Błąd: Brak klucza OPENAI_API_KEY w zmiennych środowiskowych.")
        print("Utwórz plik .env i dodaj wpis: OPENAI_API_KEY=twoj-klucz-tutaj")
        return

    # Inicjalizacja modelu językowego
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Lista dostępnych narzędzi
    tools = [get_current_time, calculator]

    # Definicja promptu dla agenta
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Jesteś pomocnym asystentem. Masz dostęp do narzędzi: {tool_names}.\nUżyj ich, aby odpowiedzieć na pytanie użytkownika."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Tworzenie agenta
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Przykładowe zapytanie wymagające obu narzędzi
    query = "Która jest teraz godzina i ile to jest 123 razy 4?"
    print(f"\n--- Zapytanie: {query} ---\n")
    
    response = agent_executor.invoke({"input": query})
    
    print(f"\n--- Odpowiedź agenta: ---\n{response['output']}")

if __name__ == "__main__":
    main()
