from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),
    path('newgame/', views.newGameForm, name='newgame'),
    path('newUser/', views.newUser, name='newUser'),
    path('gotUserInfo/', views.gotUserInfo, name='gotUserInfo'),
    path('accounts/', include('django.contrib.auth.urls')),
]
