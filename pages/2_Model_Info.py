import streamlit as st
import requests

st.set_page_config(
    page_title="Predict",
    page_icon="👋",
)

params = {'model_id' : '20220901_193009_IJTD'}

brain_signals_api = 'http://127.0.0.1:8000/model'
response = requests.get(brain_signals_api, params=params)

prediction = response.json()

st.json(prediction)
