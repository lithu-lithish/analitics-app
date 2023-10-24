import pandas as pd
from datetime import timedelta


def filter_orders_by_date(df, start_date, end_date, datetime_column):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df[datetime_column] = pd.to_datetime(df[datetime_column]) + timedelta(hours=5, minutes=30)
    filtered_data = df[(df[datetime_column]>=start_date) & (df[datetime_column]<=end_date)]
    filtered_data[datetime_column] = pd.to_datetime(filtered_data[datetime_column])
    return filtered_data