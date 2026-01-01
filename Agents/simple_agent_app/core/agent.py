from langchain.agents import create_agent
from .config import OPENAI_API_KEY


def get_agent(model_name: str = "gpt-5"):
    """
    Initializes and returns a LangChain agent.
    """
    agent = create_agent(model_name)
    return agent


def run_agent(agent, prompt: str, style: str = "technical", verbosity: str = "detailed"):
    """
    Executes a prompt on the agent and returns
    the final generated text.
    """

    result = agent.invoke(
        {
            "messages": [{"role": "user", "content": prompt}],
            "user_preferences": {
                "style": style,
                "verbosity": verbosity,
            },
        }
    )

    messages = result.get("messages", [])
    if not messages:
        return "No response returned."

    return messages[-1].content
