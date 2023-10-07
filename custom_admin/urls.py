from django.urls import path
from . import views


urlpatterns = [
    path('', views.custom_admin, name='custom_admin'),
]
