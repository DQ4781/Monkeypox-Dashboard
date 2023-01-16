import plotly.express as px
import json
from data import *
import streamlit as st


with open('usState.json') as json_file:
    file = json.load(json_file)

cases = px.choropleth_mapbox(data_frame=state_total,
                           geojson=file,
                           featureidkey="properties.NAME",
                           locations="Location",
                           color_continuous_scale="Viridis", 
                           range_color=(0,3000), 
                           mapbox_style="carto-positron", 
                           zoom=3, 
                           center={"lat": 37.0902, "lon": -95.7129}, 
                           opacity=0.5, 
                           color='Cases', 
                           labels={'Cases':'Cases Recorded'})
#cases.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


vac = px.choropleth_mapbox(data_frame=state_vac,
                           geojson=file,
                           featureidkey="properties.NAME",
                           locations="Reporting Jurisdictions",
                           color_continuous_scale="Viridis", 
                           range_color=(300,100000), 
                           mapbox_style="carto-positron", 
                           zoom=3, 
                           center={"lat": 37.0902, "lon": -95.7129}, 
                           opacity=0.5, 
                           color='Total', 
                           labels={'Total':'Vaccines Administered'})
#vac.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

def drawCaseMap():
    st.plotly_chart(cases, use_container_width=False)

def drawVacMap():
    st.plotly_chart(vac, use_container_width=False)
