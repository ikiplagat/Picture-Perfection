from django.core.checks import messages
from photos.models import Category, Image, Location
from django.shortcuts import render

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {"images":images, "location":location, "category":category})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def get_category(request, category_id):
    category = Category.objects.get(id = category_id)
    images = Image.search_by_category(category)
    return render(request, 'all-photos/category.html', {"images":images})

def get_location(request, location_id):
    location = Location.objects.get(id = location_id)
    images = Image.search_by_location(location)
    return render(request, 'all-photos/category.html', {"images":images})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term.lower())
        # searched_images = Image.search_by_location(search_term.lower())
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message":message, "images":searched_images})
    
