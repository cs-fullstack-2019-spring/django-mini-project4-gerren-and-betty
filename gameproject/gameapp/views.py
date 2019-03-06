from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameModel
<<<<<<< HEAD
from .forms import GameForm


# Create your views here.
=======
from .forms import CollectorForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return HttpResponse("index")


# function injects list into mygames.html
>>>>>>> e8df464fcd620ab816758cf7aae21db3e37ae897
@login_required
def mygames(request):
    list_of_games = GameModel.objects.filter(name=request.user)

    context = {'list_of_games': list_of_games}
    return render(request, 'gameapp/mygames.html', context)

<<<<<<< HEAD
# def newGameForm(request):
#     if(request.method == "POST"):
#         print("The new info has been updated.")
#         name = request.Post["name"]
#         developer = request.Post["developer"]
#         dateMade = request.Post["dateMade"]
#         ageLimit = request.Post["ageLimit"]
#         collector = request.Post["collector"]
#     return render(request, 'gamesapp/mygames.html', {'gameform': newGameForm})

=======
# test for index
>>>>>>> e8df464fcd620ab816758cf7aae21db3e37ae897
def index(request):
    return HttpResponse('index')


# function to create new user (collectorform) and redirect to index
def newUser(request):
    form = CollectorForm(request.POST or None)
    context = {
        "form": form
    }

    if request.method == 'POST':
        User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        form.save()
        print("New User Created")

    return render(request, "gameapp/newUser.html", context)
