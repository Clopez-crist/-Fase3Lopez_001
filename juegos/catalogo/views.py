from django.shortcuts import render
from .models import Game
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            massage.succes(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'catalogo/register.html', context)


def index(request):
    num_games = Game.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_games': num_games},
    )



def categoria(request):

    return render(
        request,
        'categoria.html',
    )


def mjrjuego(request):

    return render(
        request,
        'mjrjuego.html',
    )


def retrogame(request):

    return render(
        request,
        'retro.html',
    )


def formulario(request):

    return render(
        request,
        'formulario.html',
    )






class GameListView(generic.ListView):
    model = Game
    paginate_by = 10



class GameDetailView(generic.DetailView):
    model = Game





class GameCreate(CreateView):
    model= Game
    fields= '__all__'

class GameUpdate(UpdateView):
    model= Game
    fields= ['Nombre','Creador','Descripción']

class GameDelete(DeleteView):
    model= Game
    success_url = reverse_lazy('games')