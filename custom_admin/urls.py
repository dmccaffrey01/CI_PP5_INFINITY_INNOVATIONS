from django.urls import path
from . import views


urlpatterns = [
    path('', views.custom_admin, name='custom_admin'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('brands/add/', views.add_brand, name='add_brand'),
    path('brands/edit/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
]
