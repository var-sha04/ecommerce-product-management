from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add/', views.product_create, name='product_create'),
    path('edit/<int:id>/', views.product_update, name='product_update'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
]