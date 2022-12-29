import streamlit as st
import pandas as pd
from data import *


## PAGE INFO
st.set_page_config(
    page_title="Monkeypox Dashboard",
    page_icon="🛖",
    layout="wide"
)
st.sidebar.success("Select a page above.")
st.title("US mpox Dashboard")

def overviewModule():
    st.header("Overview")
    
    tab1, tab2, tab3 = st.tabs(["All Time", "Last Month", "Last Week"])

    dates = [[nation_cum.iloc[-1], gender_tests.iloc[-1]], 
            [nation_cum.iloc[-30], gender_tests.iloc[-4]], 
            [nation_cum.iloc[-7], gender_tests.iloc[-2]]]
    deltas = [(dates[0][0]['Cumulative Cases']-dates[1][0]['Cumulative Cases']),(dates[0][0]['Cumulative Cases']-dates[2][0]['Cumulative Cases'])] 
    genderDates = gender_tests.index.tolist()

    # All Time
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Total Cases")
            st.metric(label=f"Reporting as of {dates[0][0]['epi_date_V2']}", value=dates[0][0]['Cumulative Cases'])
        with col2:
            st.subheader("Total Tests")
            st.metric(label=f"Reporting as of {genderDates[-1]}", value=gender_tests['Total_Tests'].sum())
    # Last Month
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Cases")
            st.metric(label=f"Reporting as of {dates[1][0]['epi_date_V2']}",value=deltas[0])
        with col2:
            st.subheader("Tests")
            st.metric(label=f"Reporting as of {genderDates[-4]}",value=dates[1][1]['Total_Tests'])
    # Last Week
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Cases")
            st.metric(label=f"Reporting as of {dates[2][0]['epi_date_V2']}",value=deltas[1])
        with col2:
            st.subheader("Tests")
            st.metric(label=f"Reporting as of {genderDates[-2]}",value=dates[2][1]['Total_Tests'])


def main():
    overviewModule()


main()

st.markdown(
    """
        ## Background
        Monkeypox is a zoonotic viral infection that is extremely transmissible and is [currently declared a public health emergency of internation concern by the WHO](https://www.who.int/europe/news/item/23-07-2022-who-director-general-declares-the-ongoing-monkeypox-outbreak-a-public-health-event-of-international-concern).
        More than 100 countries have reported cases of Monkeypox and the most recent 2022 outbreak represents the first time that Monkeypox has had widespread transmission
        outside of West Africa. Those infected with Monkeypox may develop rashes and flu-like symptoms within three weeks of exposure. Currently, there are no approved 
        therapeutics or vaccines for Monkeypox specficially, but antiviral treatments and vaccines for smallpox have been approved to treat Monkeypox by the FDA.
    """
    )






