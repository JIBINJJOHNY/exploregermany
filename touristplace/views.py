from django.shortcuts import render,redirect,get_object_or_404
from .models import State,TouristPlace,TouristPlaceImage,Review
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
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
        place.average_rating = Review.objects.filter(tourist_place=place).aggregate(avg_rating=Avg('rating'))['avg_rating']

    context = {
        'state': state,
        'tourist_places': tourist_places,
    }

    return render(request, 'state_detail.html', context)


@login_required
def place_details(request, place_id):
    place = get_object_or_404(TouristPlace, pk=place_id)
    tourist_place = TouristPlace.objects.get(pk=place_id)
    default_image = TouristPlaceImage.objects.filter(touristplace=place, default_image=True).first()
    place_image_url = default_image.image_url if default_image else None

    # Retrieve reviews associated with the tourist place
    reviews = Review.objects.filter(tourist_place=place)

    return render(request, 'place_detail.html', {'place': place, 'place_image_url': place_image_url, 'reviews': reviews})

def get_large_image(request, image_id):
    try:
        image = TouristPlaceImage.objects.get(id=image_id)
        return JsonResponse({'image_url': image.image.url})
    except TouristPlaceImage.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)
