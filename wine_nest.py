import pandas as pd

'''
# PANDAS CHEAT SHEET: THE CORE 5 DRILLS

# 1. BOOLEAN MASKING (The Filter)
# Filter rows based on conditions (wrap each condition in parentheses if using & or |)
filtered_df = df[df['price'] > 50]

# 2. GROUPBY WITH NAMED AGGREGATION (The Summarizer)
# Split data by category and compute multiple summary stats into a new table
summary_df = df.groupby('country').agg(
    avg_price=('price', 'mean'),
    max_points=('points', 'max'),
    wine_count=('winery', 'count')
)

# 3. THE .TRANSFORM() PATTERN (The Group Mutate)
# Compute a group metric and broadcast it back to every individual row
df['country_avg_price'] = df.groupby('country')['price'].transform('mean')

# 4. METHOD CHAINING WITH .ASSIGN() (The Pipeline)
# Append multiple columns in a single, continuous flow using lambda
df_piped = df.assign(
    avg_points=lambda x: x.groupby('country')['points'].transform('mean'),
    min_points=lambda x: x.groupby('country')['points'].transform('min')
)

# 5. MULTI-COLUMN SORTING (The Arranger)
# Order data hierarchically (mixing ascending and descending directions)
sorted_df = df.sort_values(
    by=['price', 'points'], 
    ascending=[False, True]
)
'''

df_wine = pd.read_csv('wine_data_first150k.csv')
print(df_wine.columns)

list = ['country', 'price', 'points' ]

df_wine = df_wine[list]
print(df_wine.head())

expensive_wine = df_wine[df_wine['price'] > 200.00] 
good_wine = df_wine[df_wine['points'] > 80]

expensive_good_wine = df_wine.query("price > 200.00 and points > 80")

sorted_wine = expensive_good_wine.sort_values(
    by=['price', 'points'], 
    ascending=[False, True]
)
