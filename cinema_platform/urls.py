from django.contrib import admin
from django.urls import path, include  # Import include function

from movies.views import MoviesView  # Correct the import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
