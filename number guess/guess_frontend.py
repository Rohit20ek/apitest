import streamlit as st
import requests

st.title("Number Guessing Game")
st.write("Guess a number between 1 and 100!")

guess = int(st.number_input("enter your guess", min_value=1,max_value=100)
)
if st.button("Guess"):
    response =requests.get('http://127.0.0.1:8000/guess', params= {"guess": int(guess)})

    if response.status_code ==200:
        data = response.json()
        st.success(data["message"])
    else:
        st.error("Error: "+ str(response.status_code))
