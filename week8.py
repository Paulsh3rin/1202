# Build a dataframe that includes average sales by platform, by region.
# Business Problem

#1 Which Publisher has the highest global sales?

import pandas as pd

file_name = 'video_game_sales.csv'

# def business_problem(_topic):
#     raw_df = pd.read_csv(file_name)
    
#     publisher_df = raw_df.groupby([_topic])[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].sum()
    
#     publisher_df = publisher_df.sort_values('Global_Sales', ascending=False)
#     return publisher_df

# year_analysis = business_problem('Year')
# platform_analysis = business_problem('Platform')

# print(platform_analysis)

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot(, )  # Plot some data on the axes.



#2 Retrieve all data from the top 3 Publishers (in Global Sales)

raw_df = pd.read_csv(file_name)
print(raw_df.columns)
publisher=raw_df.groupby(['Publisher'])['Global_Sales'].sum().reset_index()
publisher=publisher.sort_values(['Global_Sales'],ascending=False)[:3] #just the top 3
l_publisher=publisher['Publisher'].to_list()
print(l_publisher)

top3_df = raw_df[raw_df['Publisher'].isin(l_publisher)]
print(top3_df) #all the data from top 3 publishers

#3 Create a reusable function that takes a df and platform and filters the results based on input.

col_name='Platform'
value_to_filter=['Year']

def df_filter(_df,_col_name, *_value):
    return _df[_df[_col_name].isin(*_value)]

print(df_filter(top3_df, col_name, value_to_filter))
