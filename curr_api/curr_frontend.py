import streamlit as st 
import requests as req

st.title('currency converter usd->inr')

amount = st.number_input("enter amount", min_value=0.0, format="%.2f")
to_currency = st.selectbox('convert to', options=['INR','USD'])

if st.button('convert'):
    payload = {
        'amount': amount,
        'to': to_currency.lower()
    }
    response = req.post('http://127.0.0.1:8000/convert', json=payload)

    if response.status_code == 200:
        data = response.json()
        st.success(f"{data.get('input', '0')} ➡️ {data.get('output', '0')}")
    else:
        st.error('Error occurred while converting currency')
