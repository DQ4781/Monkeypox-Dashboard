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
nation_cum['epi_date_V2']   = pd.to_datetime(nation_cum['epi_date_V2'], format='%Y-%m-%d', errors='coerce', utc=True)
race_percent['MMWR Week']   = pd.to_datetime(race_percent['MMWR Week'], format='%Y-%m-%d', errors='coerce', utc=True)
gender_tests['Week']        = pd.to_datetime(gender_tests['Week'], format='%Y-%m-%d', errors='coerce', utc=True)

# Reindex Gender Tests
#gender_tests.set_index('Week', inplace=True)

state_vac.set_index("Reporting Jurisdictions", inplace=True)
nyc = state_vac['Total'].loc["New York City"]
state_vac.at["New York", "Total"] += nyc
state_vac.drop(labels="New York City", inplace=True)
state_vac.reset_index(inplace=True