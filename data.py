import pandas as pd


url = "https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest_deprecated.csv"
df = pd.read_csv(url, low_memory=False)

# Collect US Confirmed Cases
df = df.loc[(df['Country'] == 'United States') & (df['Status'] == 'confirmed')]

# Drop mostly NaN attributes
usMP = df.drop(columns=[ 'Symptoms',
 'Hospitalised (Y/N/NA)',
 'Date_hospitalisation',
 'Isolated (Y/N/NA)',
 'Date_isolation',
 'Outcome',
 'Contact_comment',
 'Contact_ID',
 'Contact_location',
 'Travel_history (Y/N/NA)',
 'Travel_history_entry',
 'Travel_history_start',
 'Travel_history_location',
 'Travel_history_country',
 'Genomics_Metadata',
 'Confirmation_method',
 'Source',
 'Source_II',
 'Source_III',
 'Source_IV',
 'Source_V',
 'Source_VI',
 'Source_VII',
 'Date_entry',
 'Date_death',
 'Date_last_modified',
 'Date_onset'])

# Fill NaN values in relevant attributes as a string
usMP.fillna('', inplace=True)
