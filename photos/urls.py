from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name = 'welcome'),
    path('travel/',views.travel_photos,name='Travel'),
]
