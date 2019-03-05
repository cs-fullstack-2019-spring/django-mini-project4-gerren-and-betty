from django.urls import path, include
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('mygames/', views.mygames, name='mygames'),

    path('accounts/', include('django.contrib.auth.urls')),
]
