import pandas as pd
from datetime import datetime, timedelta


def count_unique_entries(df, column_name):
    return df[column_name].nunique()


def calculate_column_sum(df, column_name):
    return df[column_name].sum()


def groupby_sum(df, column_name, column_to_sum):
    groupby_sum = df.groupby(column_name).agg(sum=(column_to_sum, "sum"), avg=(column_to_sum, "mean")).reset_index()
    return groupby_sum


def last_n_days(df, date_column, column, no_of_days):
    current_date = datetime.now().date()
    current_date = pd.to_datetime(current_date)
    start_date = current_date - timedelta(days=no_of_days)
    start_date = pd.to_datetime(start_date)
    df[date_column] = pd.to_datetime(df[date_column]) + timedelta(hours=5, minutes=30)
    filtered_df = df[(df[date_column]>=start_date) & (df[date_column]<=current_date)]
    last_n_days_sum = filtered_df[column].sum()
    return last_n_days_sum


def daily_growth(df, date_column, column, column_to_sum):
    current_date = datetime.now().date()
    current_date = pd.to_datetime(current_date)
    start_date = current_date - timedelta(days=7)
    start_date = pd.to_datetime(start_date)
    df[date_column] = pd.to_datetime(df[date_column]) + timedelta(hours=5, minutes=30)
    filtered_df = df[(df[date_column] >= start_date) & (df[date_column] <= current_date)]
    filtered_df[date_column] = pd.to_datetime(filtered_df[date_column])
    filtered_df[column] = filtered_df[date_column].dt.date
    new_filtered_df = filtered_df.groupby(column).agg(sum=(column_to_sum, "sum")).reset_index()
    for i in range(1, len(new_filtered_df)):
        previous_sale = new_filtered_df.iloc[i - 1]['sum']
        current_sale = new_filtered_df.iloc[i]['sum']
        percentage_growth = ((current_sale - previous_sale) / previous_sale) * 100
        new_filtered_df.at[i, 'growth in %'] = percentage_growth
    return new_filtered_df


def new_and_repeat_customers(df):
    df_agg = df.groupby(["user_id"]).agg(order_count=("user_id", "count")).sort_values(by="order_count", ascending=False).reset_index()
    repeat_customers = df_agg[df_agg["order_count"]>1]
    count_of_repeat_customers = repeat_customers["user_id"].nunique()
    new_customers = df_agg[df_agg["order_count"]==1]
    count_of_new_customers = new_customers["user_id"].nunique()
    total_unique_users = df_agg["user_id"].nunique()
    return count_of_repeat_customers, count_of_new_customers, total_unique_users


def groupby_count(df, column_name):
    df[column_name] = df[column_name].str.lower()
    return df.groupby(column_name).agg(count=(column_name, "count")).sort_values(by="count", ascending=False).reset_index()


def groupby_count_int(df, column_name):
    return df.groupby(column_name).agg(count=(column_name, "count")).sort_values(by="count", ascending=False).reset_index()


def explode_df(df, column_name):
    return df.explode(column_name)


def count_occurance_in_column(df, column_name, new_column_name):
    count = df[column_name].value_counts().reset_index()
    count.columns = [new_column_name, 'Count']
    return count


def count_users_joined_last_days(df, days):
    df['created_on'] = pd.to_datetime(df['created_on'])
    current_date = datetime.now()
    days_ago = current_date - timedelta(days=days)
    users_last_days = df[df['created_on']>=days_ago]
    count_last_days = len(users_last_days)
    return count_last_days


def merge_dataframes(first_df, second_df, on_which_column):
    first_df[on_which_column] = first_df[on_which_column].astype(str)
    second_df[on_which_column] = second_df[on_which_column].astype(str)
    merged_data = first_df.merge(second_df, on=on_which_column)
    return merged_data


def calculate_revenue_by_location(df_with_amount, df_with_location, groupby_sum, merge_dataframes):
    revenue = groupby_sum(df_with_amount, 'user_id', 'amount')
    merge_revenue_filtered_location_data = merge_dataframes(df_with_location, revenue, 'user_id')
    city_wise_revenue = groupby_sum(merge_revenue_filtered_location_data, 'city', 'sum').sort_values(by='sum', ascending=False).reset_index()
    country_wise_revenue = groupby_sum(merge_revenue_filtered_location_data, 'country', 'sum').sort_values(by='sum', ascending=False).reset_index()
    state_wise_revenue = groupby_sum(merge_revenue_filtered_location_data, 'state', 'sum').sort_values(by='sum', ascending=False).reset_index()
    return city_wise_revenue, country_wise_revenue, state_wise_revenue


def avg_days_for_buying_credits(df):
    df.sort_values(by=['user_id', 'datetime'], inplace=True)
    df['difference_in_time'] = df.groupby('user_id')['datetime'].diff()
    avg_days_for_buying_credits_per_user = df.groupby('user_id')['difference_in_time'].mean().dt.days
    avg_days_for_buying_credits_per_user = pd.DataFrame(avg_days_for_buying_credits_per_user)
    average_days = avg_days_for_buying_credits_per_user['difference_in_time'].mean()
    return avg_days_for_buying_credits_per_user, average_days

def users_day_by_day(df, datetime_column, column_to_count):
    df['date_only_column'] = pd.to_datetime(df[datetime_column]).dt.date
    count_users_that_day = df.groupby('date_only_column').agg(count=(column_to_count, "count")).reset_index()
    return count_users_that_day

def avg_time_for_action(df_signup, df_action):
    df_signup = df_signup.drop_duplicates(subset="user_id", keep="first")
    df_action = df_action.drop_duplicates(subset="customer_id", keep="first")
    merged_df = pd.merge(df_signup, df_action, left_on='user_id', right_on='customer_id')
    merged_df['time_difference'] = merged_df['created_at_x'] - merged_df['created_at_y']
    return merged_df['time_difference'].dt.days