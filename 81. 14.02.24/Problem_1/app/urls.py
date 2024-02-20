from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client_products/<str:length>/<int:client_id>/', views.client_products, name='client_products'),
]