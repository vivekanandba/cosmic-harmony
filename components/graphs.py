import plotly.express as px
import numpy as np

from components.constants import class_colors

def plot_geo_with_size(df, projection):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size='mass', color='class_cat', projection=projection, color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
    fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
    fig.update_layout(showlegend=True, legend_title='Class', legend=dict(x=0.05, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig

def plot_geo_with_size_and_year(df, projection):
    df = df.sort_values(by='year', ascending=True)
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', size=np.log(df['mass']), color='class_cat', projection=projection, animation_frame='year', color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
    fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0.35, y=-0.1, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig


def plot_geo_with_size_and_year_log(df):
    fig = px.scatter(df, x='year', y='mass', color='class_cat', log_y=True,color_discrete_map=class_colors, custom_data=['mass', 'year', 'name'])
    fig.update_traces(hovertemplate='<br>'.join(['Mass: %{customdata[0]} kg', 'Year: %{customdata[1]}', 'Name: %{customdata[2]}']))
    fig.update_layout(legend_title='Class', showlegend=True, legend=dict(x=0, y=-0.2, orientation='h', bgcolor='white', bordercolor='black', borderwidth=0.1))
    return fig