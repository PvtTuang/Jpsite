from django.urls import path
from .views import search_product, add_sale

urlpatterns = [
    path('search/', search_product, name='search_product'),
    path('sale/add/<int:product_id>/', add_sale, name='add_sale'),
]
