import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewsundberg/college-basketball-dataset")

print("Path to dataset files:", path)

import os

import pandas as pd

# Find the CSV file inside the downloaded folder path
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
data_file_path = os.path.join(path, csv_files[0])

# Load the dataset into Pandas
df = pd.read_csv(data_file_path)


print(df.columns.tolist()) 

# Saves the dataframe into an Excel file in your project folder
df.to_excel("college_basketball_data.xlsx", index=False)

#  I am filtering the dataset to 5 var. - team, games won, 2 pt pct, 3 pt pct, postseason

selected_columns = ['TEAM', 'W', '2P_O', '3P_O', 'POSTSEASON', 'YEAR']
subset_df = df[selected_columns]

print(subset_df.head(5))
clean_df = subset_df.dropna()

# simplified basketball set
clean_df.to_excel('simplified basketball.xlsx', index = False)

print(clean_df.head(10))

champs_and_f4 = clean_df[clean_df['POSTSEASON'].isin(['Champions', '2ND', 'F4'])].copy()

champs_and_f4.to_excel('final four and champs.xlsx', index=False)

