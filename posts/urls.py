from django.urls import path
from posts.views import *
from notify.views import notify_line

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/update/', product_update, name='product_update'),
    path('<int:pk>/delete/', product_delete, name='product_delete'),
    path('notify/<int:product_id>/', notify_line, name='notify'),
]