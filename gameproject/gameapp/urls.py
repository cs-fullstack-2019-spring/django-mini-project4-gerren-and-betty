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

    path('newUser/', views.newUser, name='newUser'),

>>>>>>> e8df464fcd620ab816758cf7aae21db3e37ae897
    path('accounts/', include('django.contrib.auth.urls')),
]
