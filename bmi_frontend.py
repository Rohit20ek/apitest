import streamlit as st
import requests

st.title("BMI Calculator")

weight = st.number_input("weight (in kgs)", min_value=0.0)
height = st.number_input("height (in meters)", min_value=0.0)

if st.button('Calculate BMI'):
    resp=requests.post("http://127.0.0.1:8000/bmi",
                       json={'weight':weight, 'height': height}
                       )
    if resp.status_code==200:
        data = resp.json()
        st.success(f"Your BMI: **{data['bmi']}**  \nCategory: **{data['category']}**")
    else:
        st.error('error in calculating BMI please try again')   
    