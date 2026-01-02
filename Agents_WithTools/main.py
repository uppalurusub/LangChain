from agents.weather_agent import build_weather_agent
from langchain.messages import HumanMessage


def run():
    agent, system_prompt = build_weather_agent()

    while True:
        user = input("Ask about weather (or 'exit'): ")
        if user.lower() == "exit":
            break

        result = agent.invoke({
            "messages": [system_prompt, HumanMessage(user)]
        })

        print(result["messages"][-1].content)


if __name__ == "__main__":
    run()
