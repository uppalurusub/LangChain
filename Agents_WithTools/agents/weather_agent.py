from langchain.agents import create_agent
from langchain.messages import SystemMessage
from tools.weather import get_weather
from core.config import OPENAI_MODEL


def build_weather_agent():
    system_prompt = SystemMessage(
        content=[
            {
                "type": "text",
                "text": "You are an AI assistant tasked with providing weather forecast."
            }
        ]
    )

    agent = create_agent(
        OPENAI_MODEL,
        tools=[get_weather]
    )

    return agent, system_prompt
