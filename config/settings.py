import os
from dotenv import load_dotenv


def load_config():
    """Ładuje zmienne środowiskowe z pliku .env."""
    load_dotenv()


def validate_openai_key() -> bool:
    """Sprawdza obecność klucza OPENAI_API_KEY. Zwraca True jeśli jest dostępny."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Błąd: Brak klucza OPENAI_API_KEY w zmiennych środowiskowych.")
        print("Utwórz plik .env i dodaj wpis: OPENAI_API_KEY=twoj-klucz-tutaj")
        return False
    return True


def validate_google_key() -> bool:
    """Sprawdza obecność klucza Google API. Zwraca True jeśli jest dostępny."""
    if not os.getenv("GOOGLE_API_KEY") and not os.getenv("VERTEX_API_KEY"):
        print("Error: Missing GOOGLE_API_KEY or VERTEX_API_KEY in environment variables.")
        print("Create a .env file and add the entry: GOOGLE_API_KEY=your-key-here")
        return False
    return True
