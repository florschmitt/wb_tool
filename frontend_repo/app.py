import streamlit as st
import requests


st.title("Test Tool")

input1 = st.number_input("Nabenhöhe in Meter", value=0.0)
input2 = st.number_input("Jahresertrag in kWh", value=0.0)
input3 = st.number_input("Mittlere Windgeschwindigkeit", value=0.0)

#param1 = st.slider('Select a number', 1, 10, 3)

#param2 = st.slider('Select another number', 1, 10, 3)

url = 'http://localhost:8000/predict'

params = {
    'feature1': input1,  # 0 for Sunday, 1 for Monday, ...
    'feature2': input2,
    'feature3': input3
}
response = requests.get(url, params=params).json()

#st.text(response.json())
st.write(f"Weiterbetriebszeit: {response['prediction']}")
