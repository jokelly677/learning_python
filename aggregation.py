import pandas as pd

# Load the dataset into Pandas
df = pd.read_excel(r'C:\Users\josep\Desktop\Learning Code\python-warmup\simplified basketball.xlsx')

'''
'''
# find top 10% of 2pt shooting teams
n = int(len(df) * 0.10)

top_10pct_teams = df.nlargest(n, '2P_O')
print('Number of teams found:', len(top_10pct_teams))
print(top_10pct_teams[['TEAM', '2P_O', 'POSTSEASON']])

top_10pct_teams.to_excel('top 10 pct 2pt shot.xlsx', index = False)

'''
'''

# find top teams based on 2pt FGPCT
def mid_range (row):
    if row['2P_O'] >= 54.0:
        return row['TEAM']
    return None

df['elite_mid_range'] = df.apply(mid_range, axis = 1)
top_mid_range_teams = df['elite_mid_range'].dropna()
print('Number of teams found:', len(top_mid_range_teams)) 
print(top_mid_range_teams)

'''
'''


# find top 10% of 3pt shooting teams
n = int(len(df) * 0.10)

top3pt_10pct_teams = df.nlargest(n, '3P_O')
print('Number of teams found:', len(top3pt_10pct_teams))
print(top3pt_10pct_teams[['TEAM', '3P_O', 'POSTSEASON']])

top3pt_10pct_teams.to_excel('top 10 pct 3pt shot.xlsx', index = False)

'''
'''

# find top teams based on 2pt FGPCT
def long_range (row):
    if row['3P_O'] >= 38.0:
        return row['TEAM']
    return None

df['elite_long_range'] = df.apply(long_range, axis = 1)
top_long_range_teams = df['elite_long_range'].dropna()
print('Number of teams found:', len(top_long_range_teams)) 
print(top_long_range_teams)


''' 

'''
# I'm combining the datasets to find the teams that are elite in both categories

dual_threat_df = df[df['elite_mid_range'].notna() & df['elite_long_range'].notna()]

print('Number of dual-threat elite teams found:', len(dual_threat_df))
print(dual_threat_df[['TEAM', '2P_O', '3P_O']])

dual_threat_df.to_excel('Dual Threat Shooting.xlsx', index = False)
