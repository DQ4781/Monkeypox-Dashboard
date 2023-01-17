import streamlit as st
import plotly.express as px
from data import *

## PAGE INFO
st.set_page_config(
    page_title="Monkeypox Dashboard",
    page_icon="🛖",
    layout="wide"
)
st.sidebar.success("Select a page above.")
st.title("Real-Time Monkeypox (mpox) Surveillance System")
st.markdown("An Interactive Dashboard By [**CSUF's CEDDI Lab**](https://www.sampsonakwafuo.com/ceddi-lab)")


def overviewModule():
    st.header("Overview")
    
    tab1, tab2, tab3= st.tabs(["All Time", "Last Month", "Last Week"])

    dates = [
                [nation_cum.iloc[-1], gender_tests.iloc[-1]], 
                [nation_cum.iloc[-30], gender_tests.iloc[-4]], 
                [nation_cum.iloc[-7], gender_tests.iloc[-2]]
            ]
    deltas = [  (dates[0][0]['Cumulative Cases']-dates[1][0]['Cumulative Cases']),
                (dates[0][0]['Cumulative Cases']-dates[2][0]['Cumulative Cases'])
             ] 
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


def cumCases():
    st.line_chart(nation_cum, x="epi_date_V2", y="Cumulative Cases")


def dailyCases():
    st.line_chart(nation_cum, x='epi_date_V2', y='Cases')


def sevenDayAvg():
    st.bar_chart(nation_cum, x='epi_date_V2', y='7-Day Average', use_container_width=True)


def casesModule():
    col1, col2 = st.columns(2)

    with col1:
        cumCases()
    with col2:
        dailyCases()

    sevenDayAvg()


def main():
    overviewModule()
    casesModule()





main()