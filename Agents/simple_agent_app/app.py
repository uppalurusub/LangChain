import streamlit as st
from core.agent import get_agent, run_agent
from core.utils import format_response


st.set_page_config(page_title="Simple AI Agent", layout="centered")

st.title("🤖 Simple AI Agent Explorer")

st.write(
    """
    Type a question and let the agent respond.
    """
)

# Inputs
prompt = st.text_area("Enter your question:", value="Explain about AI Agents.")

style = st.selectbox(
    "Response Style:",
    ["technical", "simple", "story", "summarized"]
)

verbosity = st.selectbox(
    "Verbosity:",
    ["detailed", "brief", "bullet-points"]
)

if st.button("Run Agent"):
    with st.spinner("Thinking..."):
        try:
            agent = get_agent()
            response = run_agent(agent, prompt, style, verbosity)
            st.subheader("📝 Response")
            st.write(format_response(response))

        except Exception as e:
            st.error(f"Error: {e}")
