from utilities.main import count_unique_entries, groupby_count, explode_df, users_day_by_day
import streamlit as st
from database.pixelgen.main import images
from utilities.date_filter.main import filter_orders_by_date
from utilities.visualization import line_break, line_chart, bar_graph
from utilities.nlp.main import user_input_keywords

def image_analytics_tab(start_date, end_date):
    with open("st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    filtered_images = filter_orders_by_date(images, start_date, end_date, 'created_at')
    count_users_images_generated = count_unique_entries(filtered_images, 'customer_id')
    total_images_generated = len(filtered_images)

    st.markdown(f"<div class='container'> User Count who generated images: <span class='metric'>{count_users_images_generated}</span> </div>", unsafe_allow_html=True);line_break()
    st.markdown(f"<div class='container'>Total images generated: <span class='metric'>{total_images_generated}</span> </div>", unsafe_allow_html=True);line_break()

    count_of_image_palettes = groupby_count(filtered_images, 'palette_type')
    chart_of_image_palettes = bar_graph(count_of_image_palettes, 'palette_type', 'count', 'Images generated according to palettes', 'Palette', 'count')
    st.plotly_chart(chart_of_image_palettes)

    keywords = explode_df(filtered_images, 'keywords')
    trending_keywords = groupby_count(keywords, 'keywords').head(10)
    chart_trending_keywords = bar_graph(trending_keywords, 'keywords', 'count', 'Top overall trending keywords', 'Keywords', 'count')
    st.plotly_chart(chart_trending_keywords)

    st.write('Palette wise top 5 keywords')
    palette_wise_trending_keywords = keywords.groupby('palette_type')['keywords'].apply(lambda x: x.value_counts().nlargest(5))
    st.write(palette_wise_trending_keywords)

    st.write('Palette wise least used 5 keywords')
    palette_wise_trending_keywords = keywords.groupby('palette_type')['keywords'].apply(lambda x: x.value_counts().nsmallest(5))
    st.write(palette_wise_trending_keywords)

    chart_trending_keywords_user = bar_graph(user_input_keywords.head(20), 'removed_stopwords', 'count', 'user input keywords trend', 'Keywords', 'count')
    st.plotly_chart(chart_trending_keywords_user)

    images_that_day =  users_day_by_day(filtered_images, 'created_at', '_id')
    images_that_day_chart = line_chart(images_that_day, 'date_only_column', 'count', title='Images generated each day', x_axis_label='Date', y_axis_label='count')
    st.altair_chart(images_that_day_chart, use_container_width=True)