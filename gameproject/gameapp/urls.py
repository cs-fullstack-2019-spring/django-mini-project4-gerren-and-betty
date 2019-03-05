from django.urls import path, include
from . import views

urlpatterns = [

<<<<<<< HEAD
    path('', views.index, name='index'),
=======

    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),
<<<<<<< HEAD
    path('newUser/', views.newUser, name='newUser'),
=======

>>>>>>> b515525fa68212fe33a4081ee2956344d633b197
>>>>>>> 9c09ab609e5770232c597f9796173671eb847b26
    path('accounts/', include('django.contrib.auth.urls')),
]
