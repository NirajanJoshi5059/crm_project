from django.urls import path
from customer.views import customer_list
app_name='customer'
urlpatterns=[
    path('customer-list/', customer_list, name='customers_list'),
]