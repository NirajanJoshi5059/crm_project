from django.urls import path
from customer.views import customer_list, updateCustomer, deleteCustomer
app_name='customer'
urlpatterns=[
    path('customer-list/<str:pk>/', customer_list, name='customers_list'),
    path('update-customer/<int:id>', updateCustomer, name='update_customer'),
    path('delete-customer/<int:id>', deleteCustomer, name='delete_customer'),
]