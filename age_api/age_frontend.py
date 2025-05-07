import streamlit as st 
import requests as req

st.title('Age Calculator')

dob = st.text_input('enter your date of birth in the YYYY-MM-DD format')

if st.button('calculate'):
    if dob:
        response = req.get(f'http://127.0.0.1:8000/age?dob={dob}')
        data = response.json()

        if 'error' in data :
            st.error(data['error'])
        else:
            st.success(f'your age is {data["age"]} years old')
    else:
        st.warning('please enter your data of birth in the YYYY-MM-DD format')

