"""Web GUI for the Hello-World Greeter."""

import streamlit as st

from src.hello_world import Greeter

greeter = Greeter(
    name=st.text_input("Name"),
)

greeter.correspondent = st.text_input(
    "Correspondent", value="world", help="How to call the user"
)
greeter.tell_time = st.checkbox("Tell time when greeting", value=greeter.tell_time)
greeter.tell_weather = st.checkbox(
    "Add weather info when greeting", value=greeter.tell_time
)

col1, col2 = st.columns(2)

with col1:
    lat = st.number_input("Latitude", value=greeter.weather_location[0])

with col2:
    lon = st.number_input("Longitude", value=greeter.weather_location[1])

greeter.weather_location = lat, lon

if st.button("Say hello", disabled=not greeter.name):
    st.code(greeter.say_hello())
