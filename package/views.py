from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import State
from .models import Package,Booking
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse
from .forms import BookingForm
# Create your views here.
class PackageListView(ListView):
    model = State
    template_name = 'home.html'
    context_object_name = 'states'
class PackageDetailView(DetailView):
    model = State
    template_name = 'package_detail.html'
    context_object_name = 'state'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_id = self.kwargs['pk'] 
        context['packages'] = Package.objects.filter(state_id=state_id)
        return context

from django.core.exceptions import ValidationError

@login_required
def booking_create(request, package_id):
    package = get_object_or_404(Package, pk=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Check if the date is in the past and restrict it to the future
            booking_date = form.cleaned_data['date']
            if booking_date < timezone.now().date():
                form.add_error('date', ValidationError('Booking date must be from the current date onward'))
            # Check if the number of guests exceeds the maximum
            elif form.cleaned_data['no_of_guests'] > 6:
                form.add_error('no_of_guests', ValidationError('Maximum number of guests is 6'))
            else:
                new_booking = form.save(commit=False)
                new_booking.user = request.user
                new_booking.save()
                return redirect('booking_detail', booking_id=new_booking.id)
    else:
        initial_data = {
            'user_full_name': request.user.get_full_name(),
            'package': package,
        }
        form = BookingForm(initial=initial_data)

    return render(request, 'booking_form.html', {'form': form})

@login_required
def booking_detail(request, booking_id):
    # View to display the details of a single booking
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

@login_required
def booking_list(request):
    # View to display a list of bookings
    bookings = Booking.objects.all()
    return render(request,'booking_list.html', {'bookings': bookings})

@login_required
def select_package(request):
    states = State.objects.all()
    packages = Package.objects.all()
    
    return render(request, 'select_package.html', {'states': states, 'packages': packages})
def booking_form(request):
    if request.method == 'POST':
        # Process the form data and save the booking
        state_id = request.POST['state']
        package_id = request.POST['package']
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.state_id = state_id
            new_booking.package_id = package_id
            new_booking.user = request.user  # Set the user to the currently logged-in user
            new_booking.save()
            return redirect('booking_detail', booking_id=new_booking.id)
    else:
        # Render the booking form template
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})

def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', booking_id=booking_id)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'update_booking.html', {'form': form, 'booking': booking})

def delete_booking(request, booking_id):
    # Logic to delete the booking with the given ID
    booking = get_object_or_404(Booking, pk=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    
    return render(request, 'booking_confirm_delete.html', {'booking': booking})

def package_list(request):
    states = State.objects.all()
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'states': states, 'packages': packages})

