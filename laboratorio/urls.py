from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_list, name='home'),
    path('create/', views.laboratorio_create, name='laboratorio_create'),
    path('<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'),
    path('<int:pk>/update/', views.laboratorio_update, name='laboratorio_update'),
    path('<int:pk>/confirm_delete/', views.laboratorio_confirm_delete, name='laboratorio_confirm_delete'),
    path('<int:pk>/delete/', views.laboratorio_delete, name='laboratorio_delete'),
]
