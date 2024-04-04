from django.shortcuts import render
from .models import Movie
# Create your views here.
def get_index_page(request):
    movie = Movie.objects.all()
    return render(request, 'movie/index.html', {'movie': movie} )

def get_movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie/movie-details.html', {'movie': movie})