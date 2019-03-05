from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GameModel


# Create your views here.
<<<<<<< HEAD
def index(request):
    return HttpResponse("index")
=======
>>>>>>> b515525fa68212fe33a4081ee2956344d633b197


@login_required
def mygames(request):
    list_of_games = GameModel.objects.filter(name=request.user)
    context = {'list_of_games': list_of_games}
    return render(request, 'gameapp/mygames.html', context)


def index(request):
    return HttpResponse('index')
