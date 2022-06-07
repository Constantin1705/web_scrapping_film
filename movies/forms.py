from django import forms
from django.forms import TextInput, Select, TimeInput

from movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = '__all__'  #Formularul va contine toate fieldurile din modelul Student
        fields = ['movie_name', 'genre', 'score']

        widgets = {
            'movie_name': TextInput(attrs={'placeholder': 'Enter movie name', 'class': 'form-control'}),
            'genre':Select(attrs={'class': 'form-control'}),
            'score': TextInput(attrs={'placeholder': 'Enter movie score', 'class': 'form-control'}),


        }
