from django.shortcuts import render,redirect,get_object_or_404
from .models import State,TouristPlace,TouristPlaceImage,Review
from package.models import Package
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from .forms import ReviewForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.db.models import F
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
    return render(request,'home.html', context)

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

    # Retrieve the two latest reviews and pass them to the template
    latest_reviews = Review.objects.filter(tourist_place=place).order_by('-created_at')[:2]

    # Retrieve the total number of reviews for the place
    total_reviews_count = Review.objects.filter(tourist_place=place).count()

    return render(request, 'place_detail.html', {
        'place': place,
        'latest_reviews': latest_reviews,
        'total_reviews_count': total_reviews_count,
    })
def get_large_image(request, image_id):
    try:
        image = TouristPlaceImage.objects.get(id=image_id)
        return JsonResponse({'image_url': image.image.url})
    except TouristPlaceImage.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)

@login_required
def add_review(request, tourist_place_id):
    tourist_place = get_object_or_404(TouristPlace, pk=tourist_place_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.tourist_place = tourist_place
            review.user = request.user
            review.rating = form.cleaned_data['rating']
            review.save()

            return redirect('view_review', tourist_place_id=tourist_place_id)
    else:
        form = ReviewForm()

    context = {
        'tourist_place': tourist_place,
        'form': form,
        'place': tourist_place,  # Include 'place' in the context
    }
    return render(request, 'add_review.html', context)
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('view_review', tourist_place_id=review.tourist_place_id)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
        'place': review.tourist_place,  # Include 'place' in the context
    }

    return render(request, 'edit_review.html', context)

@login_required
def view_reviews(request, tourist_place_id):
    tourist_place = get_object_or_404(TouristPlace, id=tourist_place_id)
    reviews = Review.objects.filter(tourist_place=tourist_place).order_by('-created_at')

    context = {
        'tourist_place': tourist_place,
        'reviews': reviews,
        'current_user': request.user,
        'place': tourist_place,
    }

    return render(request, 'view_review.html', context)


@login_required
@never_cache
def delete_review(request, tourist_place_id, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        # Handle the confirmation of deletion here if you want
        review.delete()
        return redirect('view_review', tourist_place_id=tourist_place_id)

    context = {
        'review': review,
        'tourist_place_id': tourist_place_id,
        'place': review.tourist_place,  # Include 'place' in the context
    }

    return render(request, 'delete_review.html', context)
@login_required
def account_delete(request):
    # Check if the request method is POST
    if request.method == 'POST':
        user = request.user
        # Delete the user's account
        user.delete()
        # Log the user out
        logout(request)
        # Redirect to a page after successful account deletion
        return redirect('home')
    else:
        # Render a confirmation page for account deletion
        return render(request, 'account_delete.html')
