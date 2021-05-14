from django.core.checks import messages
from photos.models import Image
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def travel_photos(request):
    return render(request, 'all-photos/travel.html')

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message":message})