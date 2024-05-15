# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import JsonResponse
from django.views import View


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movies:list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all() 
        data = [{"title": movie.title, "release_year": movie.release_year, "director": movie.director} for movie in movies]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = request.POST
        title = data.get('title')
        release_year = data.get('release_year')
        director = data.get('director')
        movie = Movie.objects.create(title=title, release_year=release_year, director=director)  
        return JsonResponse({"message": "Movie created successfully"})

