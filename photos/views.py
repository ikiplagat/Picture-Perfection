from django.core.checks import messages
from photos.models import Image
from django.shortcuts import render

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images":images})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def travel_photos(request):
    images = Image.search_by_category("travel")
    return render(request, 'all-photos/travel.html', {"images":images})

def food_photos(request):
    images = Image.search_by_category("food")
    return render(request, 'all-photos/food.html', {"images":images})

def fitness_photos(request):
    images = Image.search_by_category("fitness")
    return render(request, 'all-photos/fitness.html', {"images":images})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term.lower())
        searched_images = Image.search_by_location(search_term.lower())
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message":message, "images":searched_images})