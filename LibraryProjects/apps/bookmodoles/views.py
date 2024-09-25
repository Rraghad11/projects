
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # Ensure this points to your home.html file
