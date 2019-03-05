from django.urls import path, include
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),
    path('newUser/', views.newUser, name='newUser'),
    path('accounts/', include('django.contrib.auth.urls')),
]
