import chainlit as cl
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from config import load_config, validate_openai_key
from tools import get_current_time, calculator, get_weather

@cl.on_chat_start
async def on_chat_start():
    """Inicjalizacja agenta podczas startu czatu."""
    # Ładowanie konfiguracji
    load_config()
    
    if not validate_openai_key():
        await cl.Message(content="Brak klucza OpenAI API w konfiguracji (.env)!").send()
        return

    # Inicjalizacja modelu językowego
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Lista dostępnych narzędzi
    tools = [get_current_time, calculator, get_weather]

    # Tworzenie agenta z LangGraph
    agent = create_react_agent(
        llm,
        tools,
        prompt="Jesteś pomocnym asystentem. Użyj narzędzi, aby odpowiedzieć na pytanie użytkownika.",
    )
    
    # Zapisanie agenta i pustej historii w sesji użytkownika
    cl.user_session.set("agent", agent)
    cl.user_session.set("history", [])

@cl.on_message
async def on_message(message: cl.Message):
    """Przetwarzanie wiadomości od użytkownika."""
    agent = cl.user_session.get("agent")
    history = cl.user_session.get("history", [])
    
    if not agent:
        await cl.Message(content="Agent nie został poprawnie zainicjalizowany.").send()
        return

    # Dodanie wiadomości użytkownika do historii
    history.append(("human", message.content))
    
    # Utworzenie pustej wiadomości w UI (aby pokazać, że agent pisze)
    msg = cl.Message(content="")
    await msg.send()

    # Wywołanie agenta (asynchronicznie)
    response = await agent.ainvoke({"messages": history})
    
    # Aktualizacja historii wszystkimi wygenerowanymi wiadomościami
    cl.user_session.set("history", response["messages"])
    
    # Pobranie ostatniej wiadomości
    last_message = response["messages"][-1]
    
    # Wyświetlenie odpowiedzi w UI
    msg.content = last_message.content
    await msg.update()
