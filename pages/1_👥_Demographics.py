import streamlit as st
import matplotlib.pyplot as plt
from data import * 


st.set_page_config(
    page_title="Demographic Data",
    page_icon="👥",
    initial_sidebar_state="collapsed"
)

st.title("Graphs Go Here")


def drawPieChart():
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

    st.header("Pie Chart of Genders Affected by MPX")
    st.pyplot(fig1)


def rateOfChange(val1, val2):
    return int((val1/val2 -1) * 100)


def weeklyDifference():
    gt = gender_tests.copy(deep=True)
    gt.set_index('Week', inplace=True)

    button_label = "Select Two Weeks to Compare"
    metric_label = list(gender_tests.head())
    weeks = gender_tests['Week']

    week_button = st.multiselect(options=weeks, label=button_label)

    wk1 = list(gt.loc[min(week_button)])
    wk2 = list(gt.loc[max(week_button)])

    # Calculate Rate of Change
    tmt     = str(rateOfChange(wk1[0], wk2[0])) + "%"
    mtpr    = str(rateOfChange(wk1[1], wk2[1])) + "%"
    tft     = str(rateOfChange(wk1[2], wk2[2])) + "%"
    ftpr    = str(rateOfChange(wk1[3], wk2[3])) + "%"

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label=metric_label[1], value=wk2[0], delta=tmt)
    col2.metric(label=metric_label[2], value=wk2[1], delta=mtpr)
    col3.metric(label=metric_label[3], value=wk2[2], delta=tft)
    col4.metric(label=metric_label[4], value=wk2[3], delta=ftpr)
    

def weeklyRace():
    st.header("Weekly Percentage Difference of Race")
    st.line_chart(race_percent, x='MMWR Week', width=700, height=700)


def main():
    drawPieChart()
    weeklyRace()
    weeklyDifference()


main()
