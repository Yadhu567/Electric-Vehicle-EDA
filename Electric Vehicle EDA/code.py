#importing the libraries needed
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#read data using pandas
ev_data = pd.read_csv('/Users/anpabelt/Downloads/Electric_Vehicle_Population_Size_History_By_County_.csv')
ev_data  


#reload the data but change the Date column to date data type

ev_data = pd.read_csv('/Users/anpabelt/Downloads/Electric_Vehicle_Population_Size_History_By_County_.csv', parse_dates=['Date'])
ev_data.head()  

# Extract the day from the 'Date' column and create a new column 'day' in 'ev_data'
ev_data['day'] = ev_data['Date'].dt.day

# Extract the month from the 'Date' column and create a new column 'month' in 'ev_data'
ev_data['month'] = ev_data['Date'].dt.month

# Extract the year from the 'Date' column and create a new column 'year' in 'ev_data'
ev_data['year'] = ev_data['Date'].dt.year

# Display the DataFrame to view the changes
ev_data
# Remove commas and periods from the 'Battery Electric Vehicles (BEVs)' column to clean numeric data stored as strings
ev_data["Battery Electric Vehicles (BEVs)"] = ev_data["Battery Electric Vehicles (BEVs)"].str.replace(",", "").str.replace(".", "")

# Remove commas and periods from the 'Plug-In Hybrid Electric Vehicles (PHEVs)' column for similar reasons
ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"] = ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"].str.replace(",", "").str.replace(".", "")

# Clean the 'Electric Vehicle (EV) Total' column by removing commas and periods, preparing it for numeric analysis
ev_data["Electric Vehicle (EV) Total"] = ev_data["Electric Vehicle (EV) Total"].str.replace(",", "").str.replace(".", "")

# Remove commas and periods from 'Non-Electric Vehicle Total' to ensure the data can be treated as numeric
ev_data["Non-Electric Vehicle Total"] = ev_data["Non-Electric Vehicle Total"].str.replace(",", "").str.replace(".", "")

# Similarly, clean the 'Total Vehicles' column by removing commas and periods
ev_data["Total Vehicles"] = ev_data["Total Vehicles"].str.replace(",", "").str.replace(".", "")

# Display the DataFrame to view the changes
ev_data
# Convert 'Battery Electric Vehicles (BEVs)' column to a numeric data type
ev_data["Battery Electric Vehicles (BEVs)"] = pd.to_numeric(ev_data["Battery Electric Vehicles (BEVs)"])

# Convert 'Plug-In Hybrid Electric Vehicles (PHEVs)' column to a numeric data type
ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"] = pd.to_numeric(ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"])

# Convert 'Electric Vehicle (EV) Total' column to a numeric data type
ev_data["Electric Vehicle (EV) Total"] = pd.to_numeric(ev_data["Electric Vehicle (EV) Total"])

# Convert 'Non-Electric Vehicle Total' to a numeric data type
ev_data["Non-Electric Vehicle Total"] = pd.to_numeric(ev_data["Non-Electric Vehicle Total"])

# Convert 'Total Vehicles' column to a numeric data type
ev_data["Total Vehicles"] = pd.to_numeric(ev_data["Total Vehicles"])

# Display the Dat  
# Replace missing values in the 'County' column with 'Unknown'
ev_data['County'] = ev_data['County'].fillna('Unknown')

# Replace missing values in the 'State' column with 'Unknown'
ev_data['State'] = ev_data['State'].fillna('Unknown')
# Calculate IQR
Q1 = ev_data["Battery Electric Vehicles (BEVs)"].quantile(0.25)
Q3 = ev_data["Battery Electric Vehicles (BEVs)"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
BEV_max_limit = Q3 + 1.5 * IQR

# Calculate the median
BEV_median = ev_data["Battery Electric Vehicles (BEVs)"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Battery Electric Vehicles (BEVs)"] > BEV_max_limit, "Battery Electric Vehicles (BEVs)"] = BEV_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Battery Electric Vehicles (BEVs)"])
plt.show()  

# Calculate IQR
Q1 = ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"].quantile(0.25)
Q3 = ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
plugin_max_limit = Q3 + 1.5 * IQR

# Calculate the median
plugin_median = ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"] > plugin_max_limit, "Plug-In Hybrid Electric Vehicles (PHEVs)"] = plugin_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Plug-In Hybrid Electric Vehicles (PHEVs)"])
plt.show()

Q1 = ev_data["Electric Vehicle (EV) Total"].quantile(0.25)
Q3 = ev_data["Electric Vehicle (EV) Total"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
elect_vehicle_max_limit = Q3 + 1.5 * IQR

# Calculate the median
elect_vehicle_median = ev_data["Electric Vehicle (EV) Total"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Electric Vehicle (EV) Total"] > elect_vehicle_max_limit, "Electric Vehicle (EV) Total"] = elect_vehicle_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Electric Vehicle (EV) Total"])
plt.show()  

# Calculate IQR
Q1 = ev_data["Non-Electric Vehicle Total"].quantile(0.25)
Q3 = ev_data["Non-Electric Vehicle Total"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
non_ev_max_limit = Q3 + 1.5 * IQR

# Calculate the median
non_ev_median = ev_data["Non-Electric Vehicle Total"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Non-Electric Vehicle Total"] > non_ev_max_limit, "Non-Electric Vehicle Total"] = non_ev_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Non-Electric Vehicle Total"])
plt.show()

# Calculate IQR
Q1 = ev_data["Total Vehicles"].quantile(0.25)
Q3 = ev_data["Total Vehicles"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
vehicle_max_limit = Q3 + 1.5 * IQR

# Calculate the median
vehicle_median = ev_data["Total Vehicles"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Total Vehicles"] > vehicle_max_limit, "Total Vehicles"] = vehicle_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Total Vehicles"])
plt.show()  

# Calculate IQR
Q1 = ev_data["Percent Electric Vehicles"].quantile(0.25)
Q3 = ev_data["Percent Electric Vehicles"].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper limit for outliers
percent_max_limit = Q3 + 1.5 * IQR

# Calculate the median
percent_median = ev_data["Percent Electric Vehicles"].median()

# Replace outliers with the median
ev_data.loc[ev_data["Percent Electric Vehicles"] > percent_max_limit, "Percent Electric Vehicles"] = percent_median

# Plot the boxplot again using the updated dataset
sns.boxplot(x=ev_data["Percent Electric Vehicles"])
plt.show()

# Group data by 'County' and aggregate specified columns
ev_groupby_county = ev_data.groupby(["County"]).agg({
    "Electric Vehicle (EV) Total": "sum",  # Sum of electric vehicles per county
    "Total Vehicles": "sum",  # Sum of all vehicles per county
    "Non-Electric Vehicle Total": "sum",  # Sum of non-electric vehicles per county
    "Plug-In Hybrid Electric Vehicles (PHEVs)": "sum",  # Sum of plug-in hybrids per county
    "Battery Electric Vehicles (BEVs)": "sum",  # Sum of battery electric vehicles per county
    "Percent Electric Vehicles": "mean"  # Average percentage of electric vehicles per county
}).reset_index()

# Calculate the ratio of electric vehicles to total vehicles within each county
ev_groupby_county["Electric Vehicle Ratio"] = ev_groupby_county["Electric Vehicle (EV) Total"] / ev_groupby_county["Total Vehicles"]

# Display the resulting DataFrame

# Sort the DataFrame based on the total electric vehicles in descending order
ev_groupby_county = ev_groupby_county.sort_values(by="Electric Vehicle (EV) Total", ascending=False)

# Set up the figure size and title for better visibility and aesthetics
plt.figure(figsize=(12, 8))
plt.title("Top 10 Counties by Electric Vehicle (EV) Total")

# Rotate the x-axis labels to prevent overlap and make them easier to read
plt.xticks(rotation=90)

# Create a bar plot of the top 10 counties by electric vehicle totals
sns.barplot(data=ev_groupby_county.head(10), x="County", y="Electric Vehicle (EV) Total")

# Adjust the layout to make sure none of the plot elements are cut off
plt.tight_layout()

# Display the plot
plt.show() 

# Sort the DataFrame based on the number of Battery Electric Vehicles (BEVs) in descending order
ev_groupby_county = ev_groupby_county.sort_values(by="Battery Electric Vehicles (BEVs)", ascending=False)

# Set up the figure size and title for the plot
plt.figure(figsize=(12, 8))
plt.title("Top 10 Counties by Battery Electric Vehicles (BEVs)")

# Rotate the x-axis labels to prevent overlap and make them readable
plt.xticks(rotation=90)

# Plot the top 10 counties for Battery Electric Vehicles using seaborn's barplot
sns.barplot(data=ev_groupby_county.head(10), x="County", y="Battery Electric Vehicles (BEVs)")

# Adjust the layout to ensure all plot elements are visible and not cut off
plt.tight_layout()

# Display the plot
plt.show()  

# Sort the DataFrame by Plug-In Hybrid Electric Vehicles (PHEVs) in descending order
ev_groupby_county = ev_groupby_county.sort_values(by="Plug-In Hybrid Electric Vehicles (PHEVs)", ascending=False)

# Plot the top 10 counties with the most PHEVs
plt.figure(figsize=(12, 8))
plt.title("Top 10 Counties by Plug-In Hybrid Electric Vehicles (PHEVs)")
plt.xticks(rotation=90)
sns.barplot(data=ev_groupby_county.head(10), x="County", y="Plug-In Hybrid Electric Vehicles (PHEVs)")
plt.tight_layout()
plt.show()

# Group data by year and aggregate EV totals
ev_groupby_year = ev_data.groupby('year').agg({
    "Electric Vehicle (EV) Total": "sum",
    "Total Vehicles": "sum"
}).reset_index()

# Plot EV totals over the years
plt.plot(ev_groupby_year['year'], ev_groupby_year['Electric Vehicle (EV) Total'], color='blue', label='Electric Vehicle (EV) Total')
plt.xlabel('Year')
plt.ylabel('Electric Vehicle (EV) Total')
plt.title('Annual Growth of Electric Vehicle Adoption')
plt.legend()
plt.show()

# Create a heatmap of correlations
f, ax = plt.subplots(figsize=(9, 9))
ax.set_title('EV Sales Correlation Heat Map')
sns.heatmap(ev_corr.corr(), annot=True, robust=True, linewidths=.1, fmt='.2f', ax=ax)
plt.show()

# Create a pie chart for EV vs Non-EV
plt.figure(figsize=(8, 8))
labels = ['Electric Vehicle (EV) Total', 'Non-Electric Vehicle Total']
sizes = [ev_data['Electric Vehicle (EV) Total'].sum(), ev_data['Non-Electric Vehicle Total'].sum()]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Electric Vehicle vs Non-Electric Vehicle')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Create a pie chart for BEVs vs PHEVs
plt.figure(figsize=(8, 8))
labels = ['Battery Electric Vehicles (BEVs)', 'Plug-In Hybrid Electric Vehicles (PHEVs)']
sizes = [ev_data['Battery Electric Vehicles (BEVs)'].sum(), ev_data['Plug-In Hybrid Electric Vehicles (PHEVs)'].sum()]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Battery Electric Vehicles (BEVs) vs Plug-In Hybrid Electric Vehicles (PHEVs)')
plt.axis('equal')
plt.tight_layout()
plt.show()
