from utilities.main import calculate_revenue_by_location, calculate_column_sum, groupby_sum, merge_dataframes
import streamlit as st
from database.pixelgen.main import subscription_plans, location_data
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import line_break, line_chart, bar_graph
from utilities.nlp.main import user_input_keywords

def revenue_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    filtered_subscription_plans = filter_orders_by_date(subscription_plans, start_date, end_date, 'datetime')
    filtered_location_data = filter_orders_by_date(location_data, start_date, end_date, 'created_at')
    city_wise_revenue, country_wise_revenue, state_wise_revenue = calculate_revenue_by_location(filtered_subscription_plans, filtered_location_data, groupby_sum, merge_dataframes)

    total_revenue = round(calculate_column_sum(filtered_subscription_plans, 'amount'),2)
    st.markdown(f"<div class='container'> Total revenue: <span class='metric'>{total_revenue}</span> </div>", unsafe_allow_html=True);line_break()

    city_revenue = bar_graph(city_wise_revenue, 'city', 'sum', 'City wise revenue', 'city', 'revenue')
    st.plotly_chart(city_revenue)

    state_revenue = bar_graph(state_wise_revenue, 'state', 'sum', 'state wise revenue', 'state', 'revenue')
    st.plotly_chart(state_revenue)

    country_revenue = bar_graph(country_wise_revenue, 'country', 'sum', 'country wise revenue', 'country', 'revenue')
    st.plotly_chart(country_revenue)