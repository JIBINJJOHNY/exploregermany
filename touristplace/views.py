from django.shortcuts import render
from .models import State
def home(request):
    states = State.objects.all()
    context = {
        'states': states,
    }
    return render(request, 'home.html', context)
