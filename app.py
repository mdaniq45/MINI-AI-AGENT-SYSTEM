# app/agent.py

def ai_agent(question: str) -> str:
    """
    Simple AI agent logic.
    Replace this with OpenAI, LangChain, Ollama, etc.
    """

    question = question.lower()

    if "hello" in question:
        return "Hello! How can I help you today?"

    elif "your name" in question:
        return "I am a Mini AI Agent running inside Docker."

    elif "python" in question:
        return "Python is a powerful language for AI and backend systems."

    else:
        return f"You asked: '{question}'. This is a stub AI response."