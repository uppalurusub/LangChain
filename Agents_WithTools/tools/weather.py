from langchain.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get weather information for a location."""
    if city.lower() == "hyderabad":
        return "The weather in Hyderabad is sunny with 79°F."
    return f"Sorry, I do not know the weather for {city}."
