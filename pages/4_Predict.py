import streamlit as st
import requests

st.set_page_config(
    page_title="Predict",
    page_icon="👋",
)

with st.form(key='params_for_api'):
    st.form_submit_button('Make prediction')

params = {}

brain_signals_api = 'http://127.0.0.1:8000/list'
response = requests.get(brain_signals_api, params=params)

prediction = response.json()

st.code(prediction)
