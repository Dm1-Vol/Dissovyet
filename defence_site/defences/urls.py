from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('create/', views.create_view, name='create'),
    path('edit/<int:pk>/', views.edit_view, name='edit'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
