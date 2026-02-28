"""
Agent ADK skonfigurowany do uruchomienia przez `adk web`.

Uruchomienie:
    cd c:\\Users\\Tomasz\\Desktop\\langchain
    adk web --no-reload

Otwórz http://localhost:8000 i wybierz 'adk_web_agent' z menu.
"""

import sys
import os

# Dodanie katalogu nadrzędnego do sys.path, aby importy z tools/ i config/ działały
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents import Agent
from config import load_config, validate_google_key
from tools import get_current_time_plain, calculator_plain, get_weather_plain

# Załadowanie zmiennych środowiskowych (.env)
load_config()

root_agent = Agent(
    name="helpful_assistant",
    model="gemini-2.0-flash",
    description="Pomocny asystent z dostępem do narzędzi: czas, kalkulator, pogoda.",
    instruction=(
        "Jesteś pomocnym asystentem. Odpowiadaj po polsku. "
        "Użyj narzędzi, aby odpowiedzieć na pytanie użytkownika."
    ),
    tools=[get_current_time_plain, calculator_plain, get_weather_plain],
)
