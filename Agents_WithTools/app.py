import streamlit as st
from langchain.messages import HumanMessage
from agents.weather_agent import build_weather_agent


st.set_page_config(page_title="Weather Agent", layout="centered")

st.title("🌦️ AI Weather Agent")

agent, system_prompt = build_weather_agent()

city = st.text_input("Enter a city name")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city.")
    else:
        query = f"get the weather in {city}"
        result = agent.invoke({
            "messages": [system_prompt, HumanMessage(query)]
        })

        st.success(result["messages"][-1].content)
