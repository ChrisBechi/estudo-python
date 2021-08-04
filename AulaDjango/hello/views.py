from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies

# Create your views here.
def home(request):
  filmes = Movies.objects.all()

  cinemas = ['Paulista', 'Faria lima', 'Jardim']
  title = 'Cineminha'
  return render(request, 'hello/index.html', {'title':title, 'filmes': filmes, 'cinemas': cinemas})