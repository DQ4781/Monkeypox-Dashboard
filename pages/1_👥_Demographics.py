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

# Assumes that wk1 & wk2 are gender_tests rows
def calculateRateofChange(wk1, wk2):
    tmt     = str(rateOfChange(wk1[1], wk2[1])) + "%"
    mtpr    = str(rateOfChange(wk1[2], wk2[2])) + "%"
    tft     = str(rateOfChange(wk1[3], wk2[3])) + "%"
    ftpr    = str(rateOfChange(wk1[4], wk2[4])) + "%"

    return [tmt, mtpr, tft, ftpr] 

# labels=... uses a gender_tests.head()
# values=... the later week row
# deltas=... comes from calculateRateOfChange
def displayMetrics(labels,values,deltas,single):
    col1, col2, col3, col4 = st.columns(4)

    if not single:
        col1.metric(label=labels[1], value=values[1],           delta=deltas[0])
        col2.metric(label=labels[2], value=str(values[2])+"%",  delta=deltas[1])
        col3.metric(label=labels[3], value=values[3],           delta=deltas[2])
        col4.metric(label=labels[4], value=str(values[4])+"%",  delta=deltas[3])
    else:
        col1.metric(label=labels[1], value=values[1]           )
        col2.metric(label=labels[2], value=str(values[2])+"%"  )
        col3.metric(label=labels[3], value=values[3]           )
        col4.metric(label=labels[4], value=str(values[4])+"%"  )


def weeklyDifference():

    button_label = "Select Two Weeks to Compare"
    metric_label = list(gender_tests.head())
    weeks = gender_tests['Week']

    # Retrieves the first & last week rows
    dfWk1 = gender_tests.iloc[0]
    dfWk2 = gender_tests.iloc[-1]

    week_button = st.multiselect(options=weeks, label=button_label)

    if len(week_button) == 0:
        deltas = calculateRateofChange(wk1=dfWk1, wk2=dfWk2)
        displayMetrics(labels=metric_label,values=dfWk2,deltas=deltas,single=False)
    elif len(week_button) == 1:
        displayMetrics(labels=metric_label, values=week_button[0], deltas=None, single=True)
    elif len(week_button) == 2:
        x = min(week_button)
        y = max(week_button)

        gender_tests.set_index('Week', inplace=True)
        minRow = gender_tests.loc[x]
        maxRow = gender_tests.loc[y]
        gender_tests.reset_index(inplace=True)
        
        deltas = calculateRateofChange(wk1=minRow, wk2=maxRow)
        displayMetrics(labels=metric_label, values=maxRow, deltas=deltas, single=False)
    else:
        st.error("Too many arguments!", icon="🚨")
    

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

    cumCases()
    dailyCases()
    sevenDayAvg()


main()
