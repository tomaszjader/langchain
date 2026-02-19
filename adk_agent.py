import os
from datetime import datetime
from dotenv import load_dotenv
from google_adk import LlmAgent, Tool

# Load environment variables
load_dotenv()

# Define tools
def get_current_time():
    """Returns the current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")

def calculator(expression: str):
    """Calculates the result of a simple mathematical expression. The argument should be an expression, e.g., '2 + 2'."""
    try:
        # NOTE: eval() is used here for simplicity.
        # In a production environment, use safer methods (e.g., numexpr).
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"

def main():
    # Check for API key (ADK usually looks for GOOGLE_API_KEY or VERTEX_API_KEY)
    if not os.getenv("GOOGLE_API_KEY") and not os.getenv("VERTEX_API_KEY"):
        print("Error: Missing GOOGLE_API_KEY or VERTEX_API_KEY in environment variables.")
        print("Create a .env file and add the entry: GOOGLE_API_KEY=your-key-here")
        return

    # Initialize the agent
    agent = LlmAgent(
        name="helpful_assistant",
        model="gemini-1.5-flash",  # Or another available model
        instruction="You are a helpful assistant. You have access to tools. Use them to answer the user's question.",
        tools=[get_current_time, calculator]
    )

    # Example query requiring both tools
    query = "Która jest teraz godzina i ile to jest 123 razy 4?"
    print(f"\n--- Query: {query} ---\n")

    # Run the agent
    # ADK agents are typically run synchronously for simple tasks, or via a runner.
    # checking documentation for simple invocation... 
    # Usually it's agent.run(input) or similar. 
    # Based on general ADK patterns, let's try a direct run.
    try:
        response = agent.run(query)
        print(f"\n--- Agent Response: ---\n{response}")
    except Exception as e:
        print(f"\n--- Error running agent: ---\n{e}")

if __name__ == "__main__":
    main()
