import pandas as pd



state_total = pd.read_csv("csv/stateCase.csv")
nation_cum  = pd.read_csv("csv/7dayAvg.csv")
state_vac   = pd.read_csv("csv/vaccines.csv")
gender_tests = pd.read_csv("csv/labTests.csv")
gender_confirm = pd.read_csv("csv/genders.csv")
race_percent = pd.read_csv("csv/ethincity.csv")
symptoms = pd.read_csv("csv/symptoms.csv")

# Drop US territories; only want Continental US
state_total.drop([0,53,40], inplace=True)
state_vac.drop([0,1,2,57], inplace=True)

# Reformat calendar dates to ISO 8601 
nation_cum['Epi_date_V3']   = pd.to_datetime(nation_cum['Epi_date_V3']).dt.date
race_percent['MMWR Week']   = pd.to_datetime(race_percent['MMWR Week']).dt.date
gender_tests['Week']        = pd.to_datetime(gender_tests['Week']).dt.date

# Reindex
gender_tests.set_index('Week', inplace=True)

# Create new sum columns
gender_tests = gender_tests.assign(Total_Tests=gender_tests['Total Male Tests']+gender_tests['Total Female Tests'])

# Add NYC to NY's total vaccine count
state_vac.set_index("Reporting Jurisdictions", inplace=True)
nyc = state_vac['Total'].loc["New York City"]
state_vac.at["New York", "Total"] += nyc
state_vac.drop(labels="New York City", inplace=True)
state_vac.reset_index(inplace=True)