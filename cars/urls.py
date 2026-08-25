from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('compare/', views.CompareView.as_view(), name='compare'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('mainAdmin/' , admin.site.urls)
]