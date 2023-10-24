from utilities.main import avg_time_for_action
import streamlit as st
from database.pixelgen.main import user_details, images
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import line_break, line_chart, bar_graph
from utilities.nlp.main import user_input_keywords

def actions_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    filtered_images = filter_orders_by_date(images, start_date, end_date, 'created_at')
    image_generation_time = avg_time_for_action(user_details, filtered_images)
    image_generation = (round(image_generation_time.mean(),2) * -1)
    st.markdown(f"<div class='container'> Avg time between image generation and signup: <span class='metric'>{image_generation}</span> </div>", unsafe_allow_html=True);line_break()