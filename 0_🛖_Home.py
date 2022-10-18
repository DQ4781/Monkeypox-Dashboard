import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import usMP



## PAGE INFO
st.set_page_config(
    page_title="Monkeypox Dashboard",
    page_icon="🛡",
    initial_sidebar_state="collapsed"
)
st.sidebar.success("Select a page above.")
st.title("Tracking US Monkeypox Infections in Real Time")


## HELPER FUNCTIONS
def graph_daily_infections():
    inf = {}

    for i in usMP['Date_confirmation']:
        inf[i] = 1 + inf.get(i, 0)

    df = pd.DataFrame.from_dict(inf, orient='index')
    df.rename(columns={0:"Daily Infections"}, inplace=True)
    st.line_chart(df)



graph_daily_infections()


st.markdown(
    """
        ## Background
        Monkeypox is a zoonotic viral infection that is extremely transmissible and is [currently declared a public health emergency of internation concern by the WHO](https://www.who.int/europe/news/item/23-07-2022-who-director-general-declares-the-ongoing-monkeypox-outbreak-a-public-health-event-of-international-concern).
        More than 100 countries have reported cases of Monkeypox and the most recent 2022 outbreak represents the first time that Monkeypox has had widespread transmission
        outside of West Africa. Those infected with Monkeypox may develop rashes and flu-like symptoms within three weeks of exposure. Currently, there are no approved 
        therapeutics or vaccines for Monkeypox specficially, but antiviral treatments and vaccines for smallpox have been approved to treat Monkeypox by the FDA.
    """
    )






