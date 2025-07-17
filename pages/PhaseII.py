import streamlit as st
import pandas as pd
import datetime


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
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Phase II</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>My Mood Since I Found Out About the Lab</h1>
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
data = {
    'Date': ['July 10', 'July 11', 'July 12', 'July 13', 'July 14'],
    'Mood': [5, 4, 3, 2, 0]  
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

st.line_chart(df)

st.markdown("""
**Mood Scale**  
😄 5 = Life was beautiful  
🙂 4 = Still okay  
😐 3 = Slightly worried  
😫 2 = This is getting bad  
😭 1 = Absolute despair  
""")
st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Your Mood Tracker</h1>
    """,
    unsafe_allow_html=True
)
#NEW
if 'mood_log' not in st.session_state:
    st.session_state.mood_log = pd.DataFrame(columns=["Date", "Mood"])

with st.form("mood_form"):
    date = st.date_input("Pick a date", datetime.date.today())
    mood = st.slider("How are you feeling today?  (1 = awful, 5 = amazing) ", 1, 5, 3)
    submitted = st.form_submit_button("Add to Mood Chart")

    if submitted:
        new_entry = pd.DataFrame([[date.strftime('%Y-%m-%d'), mood]], columns=["Date", "Mood"])
        st.session_state.mood_log = pd.concat([st.session_state.mood_log, new_entry], ignore_index=True)

if not st.session_state.mood_log.empty:
    mood_df = st.session_state.mood_log.copy()
    mood_df['Date'] = pd.to_datetime(mood_df['Date'])
    mood_df.sort_values('Date', inplace=True)
    mood_df.set_index('Date', inplace=True)

    st.markdown("### Your Mood Over Time")
    st.line_chart(mood_df)

    st.markdown("""
    **Mood Scale**  
    😭 1 = Terrible  
    😕 2 = Bad  
    😐 3 = Meh  
    🙂 4 = Good  
    😄 5 = Amazing  
    """)

else:
    st.info("Add a mood entry to see your mood chart!")

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>My Life Timeline :))</h1>
    """,
    unsafe_allow_html=True
)
events = [
    {"year": 2007, "event": "Born", "desc": "The year I was born!"},
    {"year": 2010, "event": "Sister Born", "desc": "My sister was born."},
    {"year": 2012, "event": "Brother Born", "desc": "My brother was born."},
    {"year": 2020, "event": "COVID Pandemic", "desc": " COVID pandemic."},
    {"year": 2021, "event": "Moved to Rabun County", "desc": "Moved to Rabun County."},
    {"year": 2025, "event": "Graduated High School", "desc": "Graduated from high school."},
]

years = [str(e["year"]) for e in events]
selected_year = st.selectbox("Select a year to see what happened", years)

selected_event = next(e for e in events if str(e["year"]) == selected_year)

st.markdown(f"### {selected_event['event']} ({selected_event['year']})")
st.write(selected_event["desc"])

st.markdown("### Timeline")
#NEW
timeline_str = ""
for e in events:
    marker = "●" if str(e["year"]) == selected_year else "○"
    timeline_str += f"{marker} {e['year']} - {e['event']}\n"
st.text(timeline_str)
st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Would You Rather!</h1>
    """,
    unsafe_allow_html=True
)

questions = [
    ("Do you prefer coffee or tea?", "Coffee", "Tea"),
    ("Are you more of an introvert or extrovert?", "Introvert", "Extrovert"),
    ("Do you like cats or dogs more?", "Cats ", "Dogs "),
    ("Are you a morning person or night owl?", "Morning ", "Night "),
]

responses = {}

st.write("adjust the plot!")
#NEW
for idx, (question, left_option, right_option) in enumerate(questions):
    st.write(f"**{question}**")
    responses[question] = st.slider(
        f"{left_option} <-> {right_option}",
        min_value=0,
        max_value=100,
        value=50,
        key=f"slider_{idx}"
    )

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
