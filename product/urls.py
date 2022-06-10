from django.urls import path
from product.views import productList
app_name='product'

urlpatterns=[ 
    path('product-list/', productList, name='product_list'),
    
]