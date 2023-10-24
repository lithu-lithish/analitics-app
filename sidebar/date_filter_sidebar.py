import streamlit as st


def date_filter_sidebar():
    start_date = st.sidebar.date_input('Start Date')
    end_date = st.sidebar.date_input('End Date')
    return start_date, end_date