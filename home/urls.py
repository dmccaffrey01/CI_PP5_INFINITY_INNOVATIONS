from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('policy/', views.policy, name='policy'),
    path('reviews/', views.reviews, name='reviews'),
    path('api/add_review', views.add_review_api, name='add_review_api'),
]
