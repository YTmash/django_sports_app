from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sport_list/', views.sport_list, name='sport_list'),
    path('contact/', views.contact, name='contact')
]