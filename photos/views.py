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
