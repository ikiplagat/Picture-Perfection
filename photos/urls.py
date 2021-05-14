from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.welcome, name = 'Welcome'),
    path('about/', views.about, name = 'About'),
    path('contact/', views.contact, name = 'Contact'),
    path('travel/',views.travel_photos, name='Travel'),
    path('food/',views.food_photos, name='Food'),
    path('fitness/',views.fitness_photos, name='Fitness'),
    path('search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
