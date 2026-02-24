"""
Punkt wejścia do projektu.
Pozwala wybrać i uruchomić jednego z dostępnych agentów.
"""
import sys


def main():
    print("=== Wybierz agenta ===")
    print("1. LangChain Agent (OpenAI)")
    print("2. ADK Agent (Google)")
    print()

    choice = input("Twój wybór (1/2): ").strip()

    if choice == "1":
        from agent_runners.langchain_agent import run_langchain_agent
        run_langchain_agent()
    elif choice == "2":
        from agent_runners.adk_agent import run_adk_agent
        run_adk_agent()
    else:
        print("Nieprawidłowy wybór. Użyj 1 lub 2.")
        sys.exit(1)


if __name__ == "__main__":
    main()
