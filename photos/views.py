from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def travel_photos(request):
    return render(request, 'all-photos/travel.html')
