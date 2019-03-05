from django.contrib import admin

# Register your models here.
from .models import CollectorModel
from .models import GameModel



admin.site.register(CollectorModel)
admin.site.register(GameModel)



