from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameModel
from .forms import CollectorForm
from django.contrib.auth.models import User


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
