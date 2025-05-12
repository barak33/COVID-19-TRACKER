import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv('owid-covid-data.csv')

# Preview the dataset
print(data.head())

# Example: Plot new cases over time
plt.figure(figsize=(10,5))
plt.plot(data['date'], data['new_cases'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title("COVID-19 Cases Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()


import pandas as pd
import requests

# Load CSV data
csv_data = pd.read_csv('owid-covid-data.csv')

# Fetch live COVID-19 data
url = "https://api.covid19api.com/summary"
response = requests.get(url)
live_data = response.json()

# Convert API data to DataFrame
live_df = pd.DataFrame(live_data['Countries'])

# Merge with existing CSV data
merged_data = pd.concat([csv_data, live_df], ignore_index=True)

# Save updated dataset
merged_data.to_csv('owid-covid-data.csv', index=False)

print("Data successfully updated!")

import streamlit as st

st.title("COVID-19 Global Data Tracker")

# Load updated data
data = pd.read_csv('owid-covid-data.csv')

# Select country for visualization
country = st.selectbox("Select a Country:", data['Hungary'].unique())

# Display key metrics
selected_data = data[data['Hungary'] == country]
st.metric("Total Cases", selected_data['TotalConfirmed'].sum())
st.metric("Total Deaths", selected_data['TotalDeaths'].sum())
st.metric("Total Recovered", selected_data['TotalRecovered'].sum())

st.line_chart(selected_data[['Date', 'NewCases']])