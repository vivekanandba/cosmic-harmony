import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

st.set_page_config(page_title='Comic Harmony', page_icon='🌠')

image_dir = Path('images')

# st.header("About this project")
# st.divider()
image = Image.open(image_dir / 'poster.jpeg')
st.image(image, caption='Cosmic Harmony', use_column_width=True)

st.divider()
st.markdown("<h1 style='text-align: center;'>A Sonification of Meteorite Impacts - Cadence of the Meteorites</h1>", unsafe_allow_html=True)
st.text("`Meteorites might be the metronome that sets the cadence of biological evolution on Earth`")
st.divider()

st.write("Hey, space enthusiasts! We're Team Cosmic Harmony, a dynamic and diverse collective of passionate individuals participating in the Immersed in the Sounds of Space challenge at the NASA Space Apps Challenge.")
st.write("Our team includes Shrishaila, the Mechanical Maestro with a flair for design and automation; Lokesh, our Python Prodigy, focusing on innovative game development; Vivek, the multifaceted Robotics and Programming Renaissance Man; Milian, our Maestro of Electric Music Production and Sound Engineering; Christabel, our storyteller, who weaves together compelling narratives and Mamta, the Artistic Soul blending electronics with aesthetic creativity. Together, we merge our skills and passions to explore the symphonic aspects of the cosmos, integrating science, art, and technology to create an extraordinary experience.")
st.write("We're excited to open our doors to like-minded individuals who share our curiosity and enthusiasm for the cosmos. Join us to collaborate and innovate, blending diverse backgrounds and skills to help more people experience the celestial symphony of the universe. Let's create cosmic magic together, exploring the unknown and bringing to life the mysterious sounds from the great beyond")

st.divider()
# Create a sample dataframe
data = {
    'Name': ['Christabel - Storyteller ', 'Milian - Audio Producer', 'Lokesh - Data Explorer', 'Shrishaila - Data Analyst', 'Mamta - Validator', 'Vivek - Integrator'],
    'Image': [image_dir / 'christabel.jpg', image_dir / 'milian.jpg', image_dir / 'lokesh.jpeg', image_dir / 'shrishaila.jpeg', image_dir / 'mamta.jpeg', image_dir / 'vivek.jpeg'],
}
df = pd.DataFrame(data)

# Display the table
col1, col2, col3 = st.columns(3)

for index, row in df.iterrows():
    if index % 3 == 0:
        col1.image(str(row['Image']), width=150)
        col1.write(row['Name'])
    elif index % 3 == 1:
        col2.image(str(row['Image']), width=150)
        col2.write(row['Name'])
    else:
        col3.image(str(row['Image']), width=150)
        col3.write(row['Name'])
st.divider()
st.markdown("<h2 style='text-align: center;'>Hackathon - Bangalore Oct - 2023</h2>", unsafe_allow_html=True)
st.divider()
st.markdown("<h3 style='text-align: center;'>References</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Dataset - NASA Meteorite Landings Data <a href>https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh</a></h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Sonification - Matt Russo Sonification in Python - Sonification with Python - How to Turn Data Into Music w Matt Russo (Part 1) <a href>https://www.youtube.com/watch?v=DUdLRy8i9qI</a></h4>", unsafe_allow_html=True)
st.divider()
st.markdown("<h4 style='text-align: center;'>Github Link - <a href>https://github.com/vivekanandba/cosmic-harmony</a></h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Project Details - <a href>https://www.spaceappschallenge.org/2023/find-a-team/cosmic-harmony</a></h4>", unsafe_allow_html=True)
st.divider()
st.markdown("<h3 style='text-align: center;'>Gallery</h3>", unsafe_allow_html=True)
st.image('images/Auditorium-Jain-University-clear.jpeg', caption='Part of the team in Jain University - Bangalore', use_column_width=True)
st.divider()
st.markdown("<h3 style='text-align: center;'>Setup</h3>", unsafe_allow_html=True)
st.image('images/coding-setup.png', caption='Coding Setup - VS Code, Python (Streamlit, Plotly, Pandas), AI - Github CoPilot, ChatGPT', use_column_width=True)
st.image('images/audio-setup-logic-pro-1.png', caption='Audio Setup - Logic Pro Valhalla reverb, Arturia piano v3', use_column_width=True)
st.image('images/audio-setup-logic-pro-2.png', caption='Audio Setup - Logic Pro Valhalla reverb, Arturia piano v3', use_column_width=True)
st.divider()



