from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import GameModel, CollectorModel
from .forms import CollectorForm, GameForm
=======
from .models import GameModel
<<<<<<< HEAD
from .forms import GameForm


# Create your views here.
=======
from .forms import CollectorForm
>>>>>>> 737853e489d4f504055a834ab2eb5a18c86f06b3
from django.contrib.auth.models import User


# Create your views here.


# function injects list into mygames.html
<<<<<<< HEAD

=======
>>>>>>> e8df464fcd620ab816758cf7aae21db3e37ae897
@login_required
>>>>>>> 737853e489d4f504055a834ab2eb5a18c86f06b3
def mygames(request):
    list_of_games = CollectorModel.objects.filter(name=request.user)

    context = {'list_of_games': list_of_games}
    return render(request, 'gameapp/mygames.html', context)

<<<<<<< HEAD

# test for index
@login_required
=======
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
>>>>>>> 737853e489d4f504055a834ab2eb5a18c86f06b3
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
