from langchain_core.tools import tool


@tool
def calculator(expression: str):
    """Oblicza wynik prostego wyrażenia matematycznego. Argumentem powinno być wyrażenie, np. '2 + 2'."""
    try:
        # UWAGA: eval() jest używany tutaj dla uproszczenia przykładu.
        # W środowisku produkcyjnym należy używać bezpieczniejszych metod (np. numexpr).
        return eval(expression)
    except Exception as e:
        return f"Błąd obliczeń: {e}"


def calculator_plain(expression: str):
    """Oblicza wynik prostego wyrażenia matematycznego (wersja bez dekoratora LangChain, dla ADK)."""
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"
