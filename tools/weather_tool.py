import os
import requests
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Zwraca obecne warunki pogodowe dla podanego miasta, korzystając z OpenWeatherMap."""
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "Błąd: Brak klucza WEATHER_API_KEY w konfiguracji."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Pogoda w {city}: {description}, temperatura: {temp}°C"
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"Nie znaleziono miasta: {city}."
        elif response.status_code == 401:
            return "Błąd autoryzacji: Nieprawidłowy klucz API OpenWeatherMap."
        return f"Błąd HTTP podczas pobierania pogody dla {city}: {str(e)}"
    except Exception as e:
        return f"Wystąpił błąd podczas pobierania pogody dla {city}: {str(e)}"

def get_weather_plain(city: str) -> str:
    """Zwraca obecne warunki pogodowe dla podanego miasta, korzystając z OpenWeatherMap. Wersja niedekorowana."""
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "Błąd: Brak klucza WEATHER_API_KEY w konfiguracji."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Pogoda w {city}: {description}, temperatura: {temp}°C"
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"Nie znaleziono miasta: {city}."
        elif response.status_code == 401:
            return "Błąd autoryzacji: Nieprawidłowy klucz API OpenWeatherMap."
        return f"Błąd HTTP podczas pobierania pogody dla {city}: {str(e)}"
    except Exception as e:
        return f"Wystąpił błąd podczas pobierania pogody dla {city}: {str(e)}"
