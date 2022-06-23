from django.urls import path
from customer.views import customer_list, updateCustomer, deleteCustomer, accountsetting
from django.conf.urls.static import static
from django.conf import settings

app_name='customer'
urlpatterns=[
    path('customer-list/<str:pk>/', customer_list, name='customers_list'),
    path('update-customer/<int:id>', updateCustomer, name='update_customer'),
    path('delete-customer/<int:id>', deleteCustomer, name='delete_customer'),
    path('account/', accountsetting, name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)