from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes, name='quotes'),
    path('orders', views.orders, name='orders'),
]