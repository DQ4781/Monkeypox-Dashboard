import plotly.express as px
import json
from data import *
import streamlit as st

st.set_page_config(
    page_title="GIS",
    page_icon="🌐"
)


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

def gisModule():
    st.header("GIS Map")
    col1, col2, col3 = st.columns(3)

    with col1:
        radio = st.radio(label='Select One of the Following', options=['Cases', 'Vaccines'])    
    
    with col2:
        state = st.selectbox(label="Select a State", options=state_total['Location'])
    
    with col3:
        if radio == 'Cases':
            st.metric(  label=f"Cases in {state}", 
                        value=state_total['Cases'][state_total['Location']==state]
                    )
        else:
            st.metric(  label=f"Vaccines Administered in {state}", 
                        value=int(state_vac['Total'][state_vac['Reporting Jurisdictions']==state])
                    )
    
    if radio == 'Cases':
        drawCaseMap()      
    else:
        drawVacMap()

def main():
    st.title("Geographic Information System")
    gisModule()

main()
