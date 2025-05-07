import streamlit as st
import requests

st.title("🌡️ Temperature Converter")

# Input from user
temp = st.number_input("Enter Temperature", value=0.0)
to = st.selectbox("Convert to", options=["Celsius", "Fahrenheit"])

if st.button("Convert"):
    # Map user choice to API param
    to_param = 'c' if to == "Celsius" else 'f'

    # Call FastAPI backend
    try:
        resp = requests.get(
            "http://127.0.0.1:8000/convert",
            params={"temp": temp, "to": to_param}
        )
        data = resp.json()

        st.success(f"✅ {data['input']} ➡️ {data['output']}")
    except Exception as e:
        st.error("❌ Problem converting. Please check backend is running.")
