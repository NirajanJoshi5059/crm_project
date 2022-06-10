from django.urls import path
from user.views import dashboard
app_name='user'

urlpatterns=[ 
    path('', dashboard, name='home'),
]