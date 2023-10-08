import streamlit as st

from components.graphs import plot_geo_with_size, plot_geo_with_size_and_year, plot_geo_with_size_and_year_log
from components.data_engg import load_data_and_clean_data   

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

df = load_data_and_clean_data()

st.subheader('Meteorites with size (in kg) animated over time')
st.plotly_chart(plot_geo_with_size_and_year(df, projection='natural earth'))

st.subheader('Meteorites with size (in kg) across time')
st.plotly_chart(plot_geo_with_size(df, projection='orthographic'))
st.plotly_chart(plot_geo_with_size(df, projection='natural earth'))

st.subheader('Meteorite Landings size of meteorite (in kg) vs year')
st.plotly_chart(plot_geo_with_size_and_year_log(df))

st.subheader("Dataframe")
df.drop(['id','class','year'], axis=1, inplace=True)
df.rename(columns={'name':'Name','mass': 'Mass (kg)', 'fall':'Fall', 'year':'Year', 'latitude':'Latitude', 'longitude': 'Longitude', 'class_cat':'Class'}, inplace=True)
# sort dataframe by index
df.reset_index(inplace=True)
df.sort_index(inplace=True)
st.dataframe(df)