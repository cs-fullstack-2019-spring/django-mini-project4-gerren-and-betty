from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD

=======
>>>>>>> 5c9a8f63fff59de5485bcf18be535788b94b9c74
    path('', views.index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),
]
