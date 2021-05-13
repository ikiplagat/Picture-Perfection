from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = 'Welcome'),
    path('about/', views.about, name = 'About'),
    path('contact/', views.contact, name = 'Contact'),
    path('travel/',views.travel_photos, name='Travel'),
]
