import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App",page_icon="🌤️")
st.title("Weather App 🥶")
st.write("Enter The City Name And Click Button To fetch weather Data")
city=st.text_input("Enter the city Name")
if st.button("Fetch Weather Data"):
    response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    if response.status_code==200:
        st.success("Weather Data Fetched Successfully")
        data=response.json()        #convert into dictionary

        #Extract Weather Information
        temperature=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        wind_speed=data["wind"]["speed"]
        weather_condition=data["weather"][0]["description"]
        name=data["name"]
        country=data["sys"]["country"]
        st.subheader(f"Weather Information for {name}, {country}")

        #create four columns to display the weather information
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)
        #col5,col6=st.columns(2)
        col1.metric("Temperature ",f"🥵{temperature} °C")
        col2.metric("Humidity ",f"💧{humidity} %")
        col3.metric("Wind Speed ",f"💨{wind_speed} m/s")
        col4.metric("Weather Condition ",f"🌤️{weather_condition}")
        # col5.metric("City Name ",f"🏙️{name}")
        # col6.metric("Country Name ",f"🌍{country}")
    else:
        st.error("City Not Found Please Enter Valid City Name")