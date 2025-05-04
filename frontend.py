import streamlit as st
import requests

st.title("Hello World API Tester")

if st.button("Call API"):
    response = requests.get("http://127.0.0.1:8000/")
    st.write(response.json())
