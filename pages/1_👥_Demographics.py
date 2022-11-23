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

# assumes that week is the index
def calculateRateofChange(wk1, wk2):
    tmt     = str(rateOfChange(wk1[0], wk2[0])) + "%"
    mtpr    = str(rateOfChange(wk1[1], wk2[1])) + "%"
    tft     = str(rateOfChange(wk1[2], wk2[2])) + "%"
    ftpr    = str(rateOfChange(wk1[3], wk2[3])) + "%"

    return [tmt, mtpr, tft, ftpr] 

def displayMetrics(labels,cmpr,values):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(label=labels[0], value=cmpr[0], delta=values[0])
    col2.metric(label=labels[1], value=cmpr[1], delta=values[1])
    col3.metric(label=labels[2], value=cmpr[2], delta=values[2])
    col4.metric(label=labels[3], value=cmpr[3], delta=values[3])  


def weeklyDifference():
    gt = gender_tests.copy(deep=True)
    gt.set_index('Week', inplace=True)

    button_label = "Select Two Weeks to Compare"
    metric_label = list(gt.head())
    weeks = gender_tests['Week']

    dfWk1 = gt.iloc[0]
    dfWk2 = gt.iloc[-1]

    week_button = st.multiselect(options=weeks, label=button_label, default=[dfWk1[0], dfWk2[0]])

    while True:
        # User deleted a date; continue displaying the default weeks
        if len(week_button) != 2: 
            rOfc = calculateRateofChange(dfWk1, dfWk2)
            displayMetrics(metric_label, dfWk2, rOfc)
        # Multiselect has two dates; display the difference
        elif len(week_button) == 2:
            wk1 = gt.loc[min(week_button)]
            wk2 = gt.loc[max(week_button)]
            rOfc = calculateRateofChange(wk1, wk2)
            displayMetrics(metric_label, wk2, rOfc)
    

def weeklyRace():
    st.header("Weekly Percentage Difference of Race")
    st.line_chart(race_percent, x='MMWR Week', width=700, height=700)

def cumCases():
    st.line_chart(nation_cum, x="epi_date_V2", y="Cumulative Cases")

def dailyCases():
    st.line_chart(nation_cum, x='epi_date_V2', y='Cases')

def sevenDayAvg():
    st.bar_chart(nation_cum, x='epi_date_V2', y='7-Day Average', use_container_width=True)

def main():
    drawPieChart()
    weeklyRace()
    weeklyDifference()


main()
