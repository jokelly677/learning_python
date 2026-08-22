'''
this is my first attempt working with python datasets. I pulled a dataset form kaggle, 
that i will need to redo in another file because of a hiccup.

'''

import pandas as pd

df = pd.read_excel("college_basketball_data.xlsx")
print(df) 


#  I am filtering the dataset to 5 var - team, games won, 2 pt pct, 3 pt pct, postseason
selected_columns = ['TEAM', 'W', '2P_O', '3P_O', 'POSTSEASON', 'YEAR']
subset_df = df[selected_columns]


clean_df = subset_df.dropna()

# simplified basketball set
clean_df.to_excel('simplified basketball.xlsx', index = False)


champs_and_f4 = clean_df[clean_df['POSTSEASON'].isin(['Champions', '2ND', 'F4'])].copy()

champs_and_f4.to_excel('final four and champs.xlsx', index=False)


