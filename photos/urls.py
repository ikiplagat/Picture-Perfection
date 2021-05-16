from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.welcome, name = 'Welcome'),
    path('about/', views.about, name = 'About'),
    path('contact/', views.contact, name = 'Contact'),
    path('search/', views.search_results, name='search_results'),
    re_path('location/(?P<location_id>\d+)', views.get_location, name='location'),
    re_path('category/(?P<category_id>\d+)', views.get_category, name='category')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
