from django.urls import path
from . import views

urlpatterns = [
    path('real/', views.all_products, name='real_products', kwargs={'type': 'real'}),
    path('digital/', views.all_products, name='digital_products', kwargs={'type': 'digital'}),
    path('<product_id>', views.product_detail, name='product_detail'),
]