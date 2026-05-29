import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 Advanced AI Chatbot")

# get API key safely from Streamlit secrets
API_KEY = os.getenv("OPENROUTER_API_KEY")

q = st.text_input("Ask me anything:")

if q:

    if not API_KEY:
        st.error("API key not found. Add it in Streamlit Secrets.")
    else:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": q}
                ]
            }
        )

        data = r.json()

        if "choices" in data:
            st.success("Response received ✅")
            st.write(data["choices"][0]["message"]["content"])
        else:
            st.error("API Error ❌")
            st.write(data)