"""Web GUI for the Hello-World Greeter."""

import streamlit as st

from src.hello_world import Greeter

greeter = Greeter(
    name=st.text_input("Name"),
)

greeter.correspondent = st.text_input("Correspondent", help="How to call the user")
greeter.tell_time = st.checkbox("Tell time when greeting")
greeter.tell_weather = st.checkbox("Add weather info when greeting")

col1, col2 = st.columns(2)

with col1:
    lat = st.number_input("Latitude")

with col2:
    lon = st.number_input("Longitude")

greeter.weather_location = lat, lon

if st.button("Say hello"):
    st.write(greeter.say_hello())
