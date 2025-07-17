
import streamlit as st
import info
import pandas as pd
# about ME
import datetime

#.streamlit/config.toml
# More accurate Streamlit background override
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
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>PB</h1>
    """,
    unsafe_allow_html=True
)
st.write("How did I end up here?")
def about_me_section():
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Dancing Script;'>About Me</h1>
    """,
    unsafe_allow_html=True
)
    st.image(info.profile_picture, width = 700)
    st.write(info.about_me)
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

about_me_section()
# links - Sidebar

def links_section():
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
    st.sidebar.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Lets Be Friends!</h1>
    """,
    unsafe_allow_html=True
)
    st.sidebar.text("Connect with me on LinkdIn")
    linkedin_link = f'<a href = "{info.my_linkedin_url}"><img src = "{info.linkedin_image_url}" alt = "LinkedIn" width = "75" height = "75" ></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html = True)
    st.sidebar.text("Follow Me on Instagram!")
    github_link = f'<a href ="{info.my_github_url}"><img src="{info.github_image_url}" alt = "Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html = True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()


# Education
# ** make the text bold
def education_section(education_data, course_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>The Beginning</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader(f"**{education_data['name']}**")
    st.write(f"**Born:**{education_data['Born']}")
    st.write(f"**Location:**{education_data['Location']}")
    st.write(f"**Siblings and Pets:**{education_data['Siblings and Pets']}")
    st.write("**SCHOOL LIFE**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "elem":"Elementary",
        "middle":"Middle",
        "High":"High School",
        "college":"College"},
        hide_index=True,        
        )
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
education_section(info.education_data, info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Hobbies and Jobs</h1>
    """,
    unsafe_allow_html=True
)
    for job_title,(job_description, image) in experience_data.items():
        expander= st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)

        st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
experience_section(info.experience_data)

# Project Section
def project_section(projects_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Skills</h1>
    """,
    unsafe_allow_html=True
)
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
project_section(info.projects_data)

#Skills

def skills_section(programming_data, spoken_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>My Hot Takes</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader("Agree or am I crazy?")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Fun Facts")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,'')}: {proficiency}")

    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
skills_section(info.programming_data, info.spoken_data)


def my_favs():
    st.markdown(
        """
        <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>💗 My Favorites 💗</h1>
        """,
        unsafe_allow_html=True
    )

    tabs = st.tabs(["**Games**", "**Movies**", "**Food**", "**Places**"])

    with tabs[0]:
        st.subheader("Favorite Games")

        # Board Games Expander
        with st.expander("Board Games"):
            st.write("- Sorry")
            st.write("- Monopoly")
            st.write("- Checkers")
            st.write("- Cards")

        #    Video Games Expander
        with st.expander("Video Games"):
            st.write("- Smash Bros")
            st.write("- Mario Kart")



    with tabs[1]:
        st.subheader("Favorite Movies")

        with st.expander("Movies List"):
            st.write("- It's a Wonderful Life")
            st.write("- Singin' in the Rain")
            st.write("- Gentlemen Prefer Blondes")
            st.write("- Top Gun")
            st.write("- Tangled")


    with tabs[2]:
        st.subheader("Favorite Foods")

        with st.expander("Foods List"):
            st.write("- Hamburgers")
            st.write("- Waffles")
            st.write("- Vietnamese")


    with tabs[3]:
        st.subheader("Favorite Places 📍")

        with st.expander("Places List"):
            st.write("- Lake Burton")
            st.write("- Lake Rabun")
            st.write("- Virginia")
            st.write("- Alligator Point")
            st.write("- St. Simons Island")


my_favs()
