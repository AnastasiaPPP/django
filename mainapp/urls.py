from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('all_clients/', views.get_clients, name='all_clients'),
    path('orders/<int:days>/', views.get_orders, name='orders'),
    path('client_orders/<int:pk>/', views.get_client_orders, name= 'client_orders'),
    path('add_good/', views.create_good, name='create_good'),
    path('all_goods/', views.get_goods, name='get_goods'),
]
