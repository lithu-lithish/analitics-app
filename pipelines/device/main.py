from utilities.main import groupby_sum, groupby_count
import streamlit as st
from database.pixelgen.main import user_device_info_data
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import pie_chart, line_break
from utilities.nlp.main import user_input_keywords

def device_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    filtered_user_device_info_data = filter_orders_by_date(user_device_info_data, start_date, end_date, 'signin_datetime')
    which_device_used = groupby_sum(filtered_user_device_info_data, 'isMobile', 'isMobile')
    count_of_mobile = which_device_used.iloc[0]["sum"]
    count_computers = len(filtered_user_device_info_data) - count_of_mobile

    st.markdown(f"<div class='container'> Count of users using computer: <span class='metric'>{count_computers}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'> count of users using mobile: <span class='metric'>{count_of_mobile}</span> </div>", unsafe_allow_html=True);line_break()

    os_used = groupby_count(filtered_user_device_info_data, 'os')
    os_used_pie = pie_chart(os_used, 'count', 'os', 'Os information')
    st.plotly_chart(os_used_pie)

    st.write('Computer os used')
    os_comp_used = groupby_count(filtered_user_device_info_data, 'osName')
    st.write(os_comp_used)

    os_comp_used = groupby_count(filtered_user_device_info_data, 'osName')
    os_comp_used_pie = pie_chart(os_comp_used, 'count', 'osName', 'Os information')
    st.plotly_chart(os_comp_used_pie)