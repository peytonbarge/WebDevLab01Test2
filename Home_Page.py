import streamlit as st
#import info
import pandas as pd
# about ME
import datetime

st.write("Peyton Barge, CS 1301")
st.markdown(
    """
    <style>
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Home Page</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: url("https://www.bing.com/th/id/OGC.a59006794e8d64a381e0f78162f202b0?o=7&pid=1.7&rm=3&rurl=https%3a%2f%2fcur.glitter-graphics.net%2fpub%2f3703%2f3703891tuiwgbkg7n.gif&ehk=5YAMQ7JSB9QxZHZr74L0ucRdnXTavcj6hEyqLl7Xyqw%3d");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align: center; color: white; font-family: Pacifico;'>My Website</h1>
    """,
    unsafe_allow_html=True
)
st.write("Welcome to my interactive website, a fun and personalized reflection of who I am. Since this lab was all about me, I took the opportunity to infuse it with as much of my personality as possible. From the vibrant pink background to the playful tone and layout, every section was designed to feel authentically me. I really enjoyed this assignment, especially the creative freedom it allowed. I used a number of different functions throughout. In my phase II tab I have 3 interactive functions. The first one is a mood tracker where you can rate your mood and see the trend. Secondly I have an interactive timeline, considering the site is about me i thought this was relevant. Last I have an interactive plot line of would you rather questions to better know the user. All interactive graphs required streamlit and pandas to be imported, the mood tracker included those two as well as datetime to be imported. Being able to customize and build on the original template made this one of the most enjoyable and expressive parts of CS 1301. ")

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

image_path = "C:/Users/pkbar/Downloads/WebDevLab01/WebDevLab01/images/homepage.jpg"
st.image(image_path, caption="My favorite moments", use_container_width=True)
image_path = "WebDevLab01/images/homepage.jpg"


#st.image(image_path, caption="My favorite moments", use_container_width=True)

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
