import pandas as pd

def get_top3_publishers(_df):
    #identify the top3
    _publisher =_df.groupby(['Publisher'])['Global_Sales'].sum().reset_index() #perform groupby
    _publisher =_publisher.sort_values(['Global_Sales'],ascending=False)[:3] #just the top 3
    return _publisher['Publisher'].to_list() #pandas to list

def df_filter(_df,_col_name, *_value):
    return _df[_df[_col_name].isin(*_value)]
