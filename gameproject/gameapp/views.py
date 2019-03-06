from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameModel, CollectorModel
from .forms import CollectorForm, GameForm
from django.contrib.auth.models import User


# Create your views here.


# function injects list into mygames.html

def mygames(request):
    list_of_games = CollectorModel.objects.filter(name=request.user)

    context = {'list_of_games': list_of_games}
    return render(request, 'gameapp/mygames.html', context)


# test for index
@login_required
def index(request):
    return HttpResponse('index')


# function to create new user (collectorform) and redirect to index
def newUser(request):
    form = CollectorForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
    else:
        print("Data not Valid.")

    return render(request, "gameapp/newUser.html", context)


# CREATES USER IN DATABASE FROM POST
def gotUserInfo(request):
    print(request.POST['username'])
    # newuser = User.objects.create_user(request.POST['username'], "", "")
    # CollectorModel.objects.create(username=request.POST)
    new_form = CollectorForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()

    return redirect('gameapp/newgame.html')

# creates new user
def newGameForm(request):
    form = GameForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        print("Your game has been saved. Check you inventory to see the new addition.")
        return redirect('mygames')
    else:
        print('Data not valid.')

    return render(request, "gameapp/newgame.html", context)
