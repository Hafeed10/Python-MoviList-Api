# urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from movies.views import MoviesView  

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/', MoviesView.as_view(), name='movies'), 
]
