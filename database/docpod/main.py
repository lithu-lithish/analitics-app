categories = get_categories_data(db_docpod)
customers = get_customers_data(db_docpod)
documents = get_documents_data(db_docpod)
plans = get_plans_data(db_docpod)
subscription_plan = get_subscription_plan_data(db_docpod)

filtered_categories = filter_orders_by_date(categories, start_date, end_date, 'created_on')
filtered_customers = filter_orders_by_date(customers, start_date, end_date, 'created_on')
filtered_documents = filter_orders_by_date(documents, start_date, end_date, 'created_on')