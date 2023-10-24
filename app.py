import streamlit as st
from database.docpod.docpod_database import db_docpod, get_categories_data, get_customers_data, get_documents_data, get_plans_data, get_subscription_plan_data
from database.pixelgen.pixelgen_database import db_pixelgen, get_user_details_data, get_subscription_plans_data, get_user_credits_data, get_images_data, get_user_location_data, get_user_device_info_data, get_referrals_data
from utilities.main import count_unique_entries, calculate_column_sum, groupby_sum, last_n_days, daily_growth, new_and_repeat_customers, groupby_count, explode_df, groupby_count_int, count_occurance_in_column, count_users_joined_last_days, merge_dataframes, calculate_revenue_by_location, avg_days_for_buying_credits, users_day_by_day, avg_time_for_action
from utilities.date_filter.main import filter_orders_by_date
from pipelines.user.main import user_analytics_tab
from pipelines.credits.main import credit_analytics_tab
from pipelines.image.main import image_analytics_tab
from pipelines.revenue.main import revenue_analytics_tab
from pipelines.actions.main import actions_analytics_tab
from pipelines.device.main import device_analytics_tab
from sidebar.date_filter_sidebar import date_filter_sidebar
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium, folium_static
import secrets
from database.TBM.TBM_database import get_orders_data, db_TBM
import pandas as pd

def check_password():

    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Password incorrect")
        return False
    else:
        return True

if check_password():

    option_selected = st.sidebar.selectbox ('Select a field', ('Pixelgen', 'Docpod', 'TBM'))
    start_date, end_date = date_filter_sidebar()

    if option_selected=='Pixelgen':

        st.title('Pixelgen Data Analysis')

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["User Analytics", "Credits Analytics", "Image Analytics", "Revenue Analytics", "Actions", "Device Info"])

        with tab1:
            st.header("User Analytics")
            user_analytics_tab(start_date, end_date)

        with tab2:
            st.header("Credits Analytics")
            credit_analytics_tab(start_date, end_date)

        with tab3:
            st.header("Image Analytics")
            image_analytics_tab(start_date, end_date)

        with tab4:
            st.header("Revenue Analytics")
            revenue_analytics_tab(start_date, end_date)

        with tab5:
            st.header ('Actions')
            actions_analytics_tab(start_date, end_date)

        with tab6:
            st.header ('Device Analytics')
            device_analytics_tab(start_date, end_date)
            


    elif option_selected=='Docpod':
        st.title('Docpod Data Analysis')

        tab1, tab2, tab3 = st.tabs(["User Analytics", "Category Analytics", "Subscription Analytics"])

        with tab1:
            st.header("User Analytics")

            st.write('Count of users')
            user_count = count_unique_entries(filtered_customers, "email")
            st.title(user_count)

            st.write('Users joined in last 30 days')
            user_count = count_users_joined_last_days(customers, 30)
            st.title(user_count)

            st.write('Users joined in last 7 days')
            user_count = count_users_joined_last_days(customers, 7)
            st.title(user_count)

        with tab2:
            st.header("Category Analytics")

            st.write('Total categories and count')
            categories_count = count_occurance_in_column(filtered_categories, 'category_name', 'Category')
            st.write(categories_count)

        with tab3:
            st.header("Subscription Analytics")

            st.write('Subscription plan division')
            subs_count = count_occurance_in_column(subscription_plan, 'plan_type', 'subscription count')
            st.write(subs_count)


    elif option_selected=='TBM':
        st.title('TBM Data Analysis')

        tab1, tab2 = st.tabs(["Item recommendations Analytics", "User Analytics"])

        with tab1:
            st.header("Item recommendations Analytics")

            orders = get_orders_data(db_TBM)
            orders['created_on'] = pd.to_datetime(orders['created_on'])
            orders = orders.sort_values(by='created_on', ascending=False)
            orders = orders.reset_index(drop=True)
            orders_exploded = orders.explode('items_ordered')

            new_df = pd.DataFrame()
            new_df['items_ordered'] = orders_exploded['items_ordered']
            df_normalized = pd.json_normalize(new_df['items_ordered'])
            df_normalized_exploded = df_normalized.explode('suborder_items_ordered')
            new_df_normalized_exploded = pd.DataFrame()
            new_df_normalized_exploded['suborder_items_ordered'] = df_normalized_exploded['suborder_items_ordered']
            df_normalized_2 = pd.json_normalize(new_df_normalized_exploded['suborder_items_ordered'])

            total_price_all_sources = df_normalized_2['price'].sum()
            #st.write(df_normalized_2)

            groupby_1 = df_normalized_2.groupby('is_recommended_item').agg(count=('is_recommended_item', "count"))
            st.write("Count of recommended items")
            st.write(groupby_1)

            groupby_2 = df_normalized_2.groupby('item_source').agg(count=('item_source', "count"))
            st.write("Count of item source")
            st.write(groupby_2)

            groupby_3 = df_normalized_2.groupby('item_source').agg(sum=('price', "sum"))
            groupby_3['percentage_of_total'] = (groupby_3['sum'] / total_price_all_sources) * 100
            st.write("Revenue from different items source")
            st.write(groupby_3)

        with tab2:
            st.write("Under construction")