from utilities.main import count_unique_entries, new_and_repeat_customers, users_day_by_day
import streamlit as st
from database.pixelgen.main import location_data, user_details, subscription_plans
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import line_break, line_chart, bar_graph


def user_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    filtered_location_data = filter_orders_by_date(location_data, start_date, end_date, 'created_at')
    filtered_subscription_plans = filter_orders_by_date(subscription_plans, start_date, end_date, 'datetime')
    city_counts = filtered_location_data['city'].value_counts().reset_index()
    city_bar_chart = bar_graph(city_counts, 'index', 'city', 'City wise user count', 'city', 'count')
    st.plotly_chart(city_bar_chart)

    user_count = count_unique_entries(user_details, "email")
    repeat_customers, new_customers, total_unique_users = new_and_repeat_customers(filtered_subscription_plans)
    user_count = count_unique_entries(user_details, "email")
    non_subscribers = user_count - total_unique_users

    st.markdown(f"<div class='container'> User Count: <span class='metric'>{user_count}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Users who subscribed: <span class='metric'>{total_unique_users}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Users who didnot subscribe: <span class='metric'>{non_subscribers}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Repeat users buying credits: <span class='metric'>{repeat_customers}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> New users buying credits: <span class='metric'>{new_customers}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Total users buying credits: <span class='metric'>{total_unique_users}</span> </div>", unsafe_allow_html=True);line_break()

    users_that_day =  users_day_by_day(user_details, 'created_at', 'user_id')
    user_chart = line_chart(users_that_day, 'date_only_column', 'count', title='User Signups', x_axis_label='Date', y_axis_label='count')
    st.altair_chart(user_chart, use_container_width=True)
    