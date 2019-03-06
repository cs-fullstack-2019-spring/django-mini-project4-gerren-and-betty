from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GameModel
from .forms import GameForm


# Create your views here.
@login_required
def mygames(request):
    list_of_games = GameModel.objects.filter(name=request.user)
    context = {'list_of_games': list_of_games}
    return render(request, 'gameapp/mygames.html', context)

# def newGameForm(request):
#     if(request.method == "POST"):
#         print("The new info has been updated.")
#         name = request.Post["name"]
#         developer = request.Post["developer"]
#         dateMade = request.Post["dateMade"]
#         ageLimit = request.Post["ageLimit"]
#         collector = request.Post["collector"]
#     return render(request, 'gamesapp/mygames.html', {'gameform': newGameForm})

def index(request):
    return HttpResponse('index')
