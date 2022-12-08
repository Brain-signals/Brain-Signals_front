import streamlit as st
import requests

st.set_page_config(
    page_title="List Models",
    page_icon="👋",
)

params = {}

brain_signals_api = 'http://127.0.0.1:8000/list'
response = requests.get(brain_signals_api, params=params)

prediction = response.json()

st.json(prediction)
