from django.urls import path, include
from . import views

urlpatterns = [

<<<<<<< HEAD
    path('', views.index, name='index'),
=======

    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),

>>>>>>> b515525fa68212fe33a4081ee2956344d633b197
    path('accounts/', include('django.contrib.auth.urls')),
]
