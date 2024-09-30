from django.urls import path
from . import views

urlpatterns = [
    path('', views.interview_list, name='interview_list'),
    path('create/', views.interview_create, name='interview_create'),
    path('delete/<int:pk>/', views.interview_delete, name='interview_delete'),
]
