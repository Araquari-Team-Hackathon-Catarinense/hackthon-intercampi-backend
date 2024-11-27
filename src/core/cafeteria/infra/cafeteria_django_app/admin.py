from django.contrib import admin

# Register your models here.
from .models import Menu, TurnstileEntrance, Cafeteria

admin.site.register(Menu)
admin.site.register(TurnstileEntrance)
admin.site.register(Cafeteria)
