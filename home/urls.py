from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
]
