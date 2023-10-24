from django.contrib import admin
from .models import State

admin.site.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
