from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index')
]
=======
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]
>>>>>>> 4bbf05e23516a562ec5383d077fd7ca5e1ec70b1
