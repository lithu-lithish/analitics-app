import streamlit as st
from utilities.main import count_unique_entries, calculate_column_sum, last_n_days, daily_growth, groupby_count_int, avg_days_for_buying_credits
from database.pixelgen.main import user_credits, user_details, subscription_plans
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import line_break, line_chart, bar_graph

def credit_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    count_users_bought_credits = count_unique_entries(user_credits, 'user_id')
    column_sum = calculate_column_sum(user_credits, 'no_of_credits')
    filtered_subscription_plans = filter_orders_by_date(subscription_plans, start_date, end_date, 'datetime')
    credits_sold = calculate_column_sum(filtered_subscription_plans, 'no_of_credits')
    last_30_days_sum = last_n_days(subscription_plans, 'datetime', 'no_of_credits', 30)
    last_7_days_sum = last_n_days(subscription_plans, 'datetime', 'no_of_credits', 7)
    avg_days_for_buying_credits_per_user, average_days = avg_days_for_buying_credits(filtered_subscription_plans)

    st.markdown(f"<div class='container'> User Count who bought credits: <span class='metric'>{count_users_bought_credits}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Active Credits: <span class='metric'>{column_sum}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Total Credits Sold: <span class='metric'>{credits_sold}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Credits Sold last 30 days: <span class='metric'>{last_30_days_sum}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Credits Sold last 7 days: <span class='metric'>{last_7_days_sum}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> Average days between buying credits: <span class='metric'>{average_days}</span> </div>", unsafe_allow_html=True);line_break()

    st.write('Daily growth chart')
    daily_growth_df = daily_growth(subscription_plans, 'datetime', 'only_date', 'no_of_credits')
    st.bar_chart(daily_growth_df.set_index('only_date')['sum'])

    purchsed_credits = groupby_count_int(subscription_plans, 'no_of_credits').head(3)
    purchsed_credits_bar_chart = bar_graph(purchsed_credits, 'no_of_credits', 'count', 'Most purchased credits', 'Credits', 'Count')
    st.plotly_chart(purchsed_credits_bar_chart)

    purchsed_credits = groupby_count_int(subscription_plans, 'no_of_credits').tail(3)
    purchsed_credits_bar_chart = bar_graph(purchsed_credits, 'no_of_credits', 'count', 'Least purchased credits', 'Credits', 'Count')
    st.plotly_chart(purchsed_credits_bar_chart)