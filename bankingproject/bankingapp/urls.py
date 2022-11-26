from datetime import datetime

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views, forms

app_name='bankingapp'
urlpatterns=[
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('form/',views.form,name='form'),
]