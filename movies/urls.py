from django.urls import path

from movies import views



urlpatterns = [
    path('list/', views.movie, name='movies'),
    path('add-movie/', views.MovieCreateView.as_view(), name='add_movie'),
]