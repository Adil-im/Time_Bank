from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Post, User
from django.contrib.auth.decorators import login_required
from .Forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages

# Create your views here.


def home(request):
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'timebank/main.html', {'posts': posts})
    
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'timebank/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                
                if user.time_credits == 0:
                    user.time_credits = 10
                    user.save()
                    messages.success(request,"You have been allocated 10 Time Credits!")
                login(request, user)
                return redirect('home')
            
                
    else:
        form = LoginForm()
    return render(request, 'timebank/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'timebank/profile.html', {'user': request.user})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # You can add user field here if you add it to Post model
            # post.user = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'timebank/create_post.html', {'form': form})