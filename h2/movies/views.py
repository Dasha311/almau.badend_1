from django.shortcuts import render
from .models import Moves
# Create your views here.
def get_index_page(request):
    moves = Moves.objects.all()
    return request(request, 'moves/index.html', {'moves': moves})
