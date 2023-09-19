from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products', kwargs={'universe': 'all'}),
    path('real/', views.all_products, name='real_products', kwargs={'universe': 'real'}),
    path('digital/', views.all_products, name='digital_products', kwargs={'universe': 'digital'}),
    path('<product_id>', views.product_detail, name='product_detail'),
]