from django.urls import path
from user.views import dashboard, login_view, register_view, logout_view
app_name='user'

urlpatterns=[ 
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/',logout_view, name='logout'),
]