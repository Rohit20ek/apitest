import streamlit as st 
import requests as req

st.title('Random Joke Generator')

if st.button('Get a random joke'):
    response= req.get('http://127.0.0.1:8000/joke')

    if response.status_code==200:
        data= response.json()
        st.success(data['joke'])
    else:
        st.error('Error occurred while fetching joke')
        
        
