import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from movies.models import Movie
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from movies.forms import MovieForm

def movie(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])
    return render(request, "movies/list.html", {'movies': movies})


class MovieCreateView(CreateView):
    template_name = 'movies/create_movie.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('home')



