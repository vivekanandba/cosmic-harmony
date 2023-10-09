import streamlit as st

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

st.markdown("<h1 style='text-align: center;'>A Sonification of Meteorite Impacts</h1>", unsafe_allow_html=True)

# st.header("Cadence of the Meteorites ")
st.divider()
# st.header("Experience the Cadence of the Meteorites")
st.markdown("<h2 style='text-align: center;'>We created this immersive experience, so it`s accessible to both, those with vision, and those who perceive beyond sight.</h2>", unsafe_allow_html=True)
st.divider()


# st.markdown("#### Chronicles of the Meteorites")

st.markdown("<h3 style='text-align: center;'>Meteorite discoveries and impacts have been a part of human history for millennia.</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Some meteorites have had significant impacts on both science and culture.</h3>", unsafe_allow_html=True)

st.divider()
st.markdown("<h2 style='text-align: center;'>Immersive Audio Visual Experience - Space Orchestra</h2>", unsafe_allow_html=True)
st.video('data/space-orchestra-correct.mp4')

st.divider()
st.markdown("<h2 style='text-align: center;'>Immersive Audio Visual Experience - Jazz Ensemble</h2>", unsafe_allow_html=True)
st.video('data/jazz-ensemble-correct.mp4')
st.divider()
st.video("data/outro.mp4")
st.divider()