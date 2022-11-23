import streamlit as st
import pandas as pd
import altair as alt
from data import *


## PAGE INFO
st.set_page_config(
    page_title="Monkeypox Dashboard",
    page_icon="🛖"
)
st.sidebar.success("Select a page above.")
st.title("Tracking US Monkeypox Infections in Real Time")


st.header("Overview")

tab1, tab2, tab3 = st.tabs(["All Time", "Last Month", "Last Week"])


# All Time, Last Month, Last Week
# --------------------------------
# Number of Cases           

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Number of Cases")
        st.caption("Testing fi this cpations is going to wrap the text around or hele im oing toi be realvery difficult")
        cumCases = nation_cum['Cumulative Cases'].iloc[-1]
        st.metric(label="Cases", value=cumCases)
    with col2:
        st.subheader("Number of Tests")
        st.caption("Testing fi this cpations is going to wrap the text around or hele im oing toi be realvery difficult")
        tests = gender_tests['Total Male Tests'].sum() + gender_tests['Total Female Tests'].sum()
        st.metric(label="Tests", value=tests)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Number of Cases Tab 2 Col1")
    with col2:
        st.subheader("Testing Tab 2 Col 2")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Testing Tab 3 Col1")
    with col2:
        st.subheader("Testing Tab 3 Col 2")








st.markdown(
    """
        ## Background
        Monkeypox is a zoonotic viral infection that is extremely transmissible and is [currently declared a public health emergency of internation concern by the WHO](https://www.who.int/europe/news/item/23-07-2022-who-director-general-declares-the-ongoing-monkeypox-outbreak-a-public-health-event-of-international-concern).
        More than 100 countries have reported cases of Monkeypox and the most recent 2022 outbreak represents the first time that Monkeypox has had widespread transmission
        outside of West Africa. Those infected with Monkeypox may develop rashes and flu-like symptoms within three weeks of exposure. Currently, there are no approved 
        therapeutics or vaccines for Monkeypox specficially, but antiviral treatments and vaccines for smallpox have been approved to treat Monkeypox by the FDA.
    """
    )






