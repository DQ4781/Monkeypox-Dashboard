import pandas as pd



state_total = pd.read_csv("/csv/data-table.csv")
nation_cum  = pd.read_csv("/csv/7dayAvg.csv")
state_vac   = pd.read_csv("/csv/vaccinesAdmin.csv")
gender_tests = pd.read_csv("/csv/nvo-data.csv")
gender_confirm = pd.read_csv("/csv/ageGender.csv")
race_percent = pd.read_csv("/csv/raceWeeklyPercent.csv")
symptoms = pd.read_csv("/csv/symptoms.csv")


state_total.drop([0,53,40], inplace=True)
state_vac.drop([0,1,2,57])
