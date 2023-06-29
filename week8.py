import pandas as pd
from week8_helper import df_filter, get_top3_publishers

#assign name to the path & read the file 
FILE_NAME = 'video_game_sales.csv'
raw_df = pd.read_csv(FILE_NAME)

#Values to filter
# COL_NAME='Global_Sales'
# to_filter = []

#function call
l_publisher = get_top3_publishers(raw_df)
print(l_publisher)
#filter dataframe
# top3_df = raw_df[raw_df['Publisher'].isin(l_publisher)]
# filtered_top3 = df_filter(top3_df, COL_NAME, to_filter)

# print(filtered_top3)
# print(filtered_top3.sort_values(by='Global_Sales', ascending=False))

