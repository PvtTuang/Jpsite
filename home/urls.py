from django.urls import path
from home.views import *
from posts.views import product_list,product_search
# ,product_search 

urlpatterns = [
    path('', home ,name='home'),
    path('posts/',product_list,name='posts'),
    path('search/',product_search,name='search'),
]