import pandas as pd  
import csv
import matplotlib.pyplot as plt


electric_vehicle_data = pd.read_csv("Electric_Vehicle_Population_Data.csv")

ev_df = pd.DataFrame(electric_vehicle_data)

print(ev_df.head())

print(ev_df.info)

# Looking at the columns in the dataframe
print(ev_df.columns)

# Checking the datatypes of the columns
print(ev_df.dtypes)

print(ev_df.describe())

# Checking for null values
print(ev_df.isnull().sum())


print(ev_df.value_counts('Make'))

print(ev_df.value_counts('Make',normalize=True))

make_df = ev_df.groupby('Make').agg({'Electric Range':'mean'})
print(make_df)

# Group the dataframe by state and then count the number of vehicles per state
state_ev_counts = ev_df.groupby('State').size().reset_index(name='EV Count')

sorted_state_ev_counts = state_ev_counts.sort_values(by='EV Count', ascending=False)

print(sorted_state_ev_counts.head())

model_year_counts = ev_df.groupby('Model Year').size().reset_index(name='EV Count')
model_year_counts = model_year_counts.sort_values(by='Model Year')
plt.figure(figsize=(10, 6))
plt.bar(model_year_counts['Model Year'], model_year_counts['EV Count'], color='skyblue')
plt.xlabel('Model Year')
plt.ylabel('Number of Electric Vehicles')
plt.title('Distribution of Electric Vehicles by Model Year')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()