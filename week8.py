# Build a dataframe that includes average sales by platform, by region.
# Business Problem #1
# Which Publisher has the highest global sales?

import pandas as pd

file_name = 'video_game_sales.csv'

def business_problem(_topic):
    raw_df = pd.read_csv(file_name)
    
    publisher_df = raw_df.groupby([_topic])[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']].sum()
    
    publisher_df = publisher_df.sort_values('Global_Sales', ascending=False)
    return publisher_df

year_analysis = business_problem('Year')
platform_analysis = business_problem('Platform')

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot(, )  # Plot some data on the axes.

# print(year_analysis)
