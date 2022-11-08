import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import *


## PAGE INFO
st.set_page_config(
    page_title="Monkeypox Dashboard",
    page_icon="🛡",
    initial_sidebar_state="collapsed"
)
st.sidebar.success("Select a page above.")
st.title("Tracking US Monkeypox Infections in Real Time")


st.line_chart(nation_cum, x="epi_date_V2", y="Cumulative Cases")



sums = [int(gender_confirm["Men"].sum()),
        int(gender_confirm["Women"].sum()),
        int(gender_confirm["Another sex/gender"].sum()),
        int(gender_confirm["Transgender women"].sum()),
        int(gender_confirm["Transgender men"].sum())           
        ]

labels = ['Men', 'Women', 'Etc', 'Transgender Women', 'Trangender Men']
colors = ['#5FCD32', '#32ACCD', '#A032CD', '#CD5332', 'crimson']
explode = [0, 0.2, 0.4, 0.6, 0.8]

fig1, ax1 = plt.subplots()
ax1.pie(sums, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, colors=colors, radius=2)
ax1.axis('equal')

fig1.legend(sums, loc="upper right")

st.pyplot(fig1)





st.markdown(
    """
        ## Background
        Monkeypox is a zoonotic viral infection that is extremely transmissible and is [currently declared a public health emergency of internation concern by the WHO](https://www.who.int/europe/news/item/23-07-2022-who-director-general-declares-the-ongoing-monkeypox-outbreak-a-public-health-event-of-international-concern).
        More than 100 countries have reported cases of Monkeypox and the most recent 2022 outbreak represents the first time that Monkeypox has had widespread transmission
        outside of West Africa. Those infected with Monkeypox may develop rashes and flu-like symptoms within three weeks of exposure. Currently, there are no approved 
        therapeutics or vaccines for Monkeypox specficially, but antiviral treatments and vaccines for smallpox have been approved to treat Monkeypox by the FDA.
    """
    )






