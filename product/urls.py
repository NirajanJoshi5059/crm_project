from django.urls import path
from product.views import productList, createOrder, updateOrder, deleteOrder

app_name='product'

urlpatterns=[ 
    path('product-list/', productList, name='product_list'),
    path('create-order/<int:id>', createOrder, name='create_order'),
    path('update-order/<int:id>',updateOrder, name='update_order'),
    path('delete-order/<int:id>', deleteOrder, name='delete_order'),
    
]