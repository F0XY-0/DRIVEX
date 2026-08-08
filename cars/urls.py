from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # landing/root — currently unrouted, TODO before deploy
    path('contact/',views.contact , name="contact") , # contact form page
    path('Home/',views.Home , name="Home") , # hero landing page (bug: renders "Home.html", file is "home.html") 
    path('main/',views.main , name="main") , # full car listing
    path('compare/',views.compare , name='compare') , 
    path('car/<int:pk>' , views.car_detail , name='car_detail') , 
]