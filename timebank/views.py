from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def home(request):
        return render(request, 'timebank/main.html')

    
    # Fetch all posts
    
