from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),
=======

    path('', views.index, name='index'),

    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),
    path('newgame/', views.newGameForm, name='newgame'),
    path('newUser/', views.newUser, name='newUser'),
<<<<<<< HEAD
    path('gotUserInfo/', views.gotUserInfo, name='gotUserInfo'),
=======

>>>>>>> e8df464fcd620ab816758cf7aae21db3e37ae897
>>>>>>> 737853e489d4f504055a834ab2eb5a18c86f06b3
    path('accounts/', include('django.contrib.auth.urls')),
]
