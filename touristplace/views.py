from django.shortcuts import render,redirect,get_object_or_404
from .models import State,TouristPlace,TouristPlaceImage
from django.contrib.auth.decorators import login_required

def account_settings(request):
   
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account_settings.html', context)

def home(request):
    states = State.objects.all()
    context = {
        'states': states,
    }
    return render(request, 'home.html', context)

@login_required
def state_detail(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    tourist_places = TouristPlace.objects.filter(state=state)

    # Calculate average ratings for each tourist place
    for place in tourist_places:
        place.average_rating = Rev.objects.filter(tourist_place=place).aggregate(avg_rating=Avg('rating'))['avg_rating']

    context = {
        'state': state,
        'tourist_places': tourist_places,
    }

    return render(request, 'state_detail.html', context)