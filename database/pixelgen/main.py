from database.pixelgen.pixelgen_database import get_user_details_data, get_user_credits_data, get_subscription_plans_data, get_images_data, get_user_location_data, get_user_device_info_data, get_referrals_data, db_pixelgen
from utilities.date_filter.main import filter_orders_by_date

user_details = get_user_details_data(db_pixelgen)
user_credits = get_user_credits_data(db_pixelgen)
subscription_plans = get_subscription_plans_data(db_pixelgen)
images = get_images_data(db_pixelgen)
location_data = get_user_location_data(db_pixelgen)
user_device_info_data = get_user_device_info_data(db_pixelgen)
referrals_data = get_referrals_data(db_pixelgen)

#filtered_user_details = filter_orders_by_date(user_details, start_date, end_date)
#filtered_user_credits = filter_orders_by_date(user_credits, start_date, end_date)
#filtered_subscription_plans = filter_orders_by_date(subscription_plans, start_date, end_date, 'datetime')
#filtered_images = filter_orders_by_date(images, start_date, end_date, 'created_at')
#filtered_location_data = filter_orders_by_date(location_data, start_date, end_date, 'created_at')
#filtered_user_device_info_data = filter_orders_by_date(user_device_info_data, start_date, end_date, 'signin_datetime')