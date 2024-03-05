from django.urls import path
from accounts.views import register, login,logout
from home.views import home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
]