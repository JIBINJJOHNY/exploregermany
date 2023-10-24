from django.shortcuts import render, redirect, get_object_or_404
from .models import State
from .models import Package
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

@login_required
def booking_create(request, package_id):
    package = get_object_or_404(Package, pk=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['date']
            if booking_date < timezone.now().date():
                form.add_error('date', ValidationError('Date cannot be in the past'))
            else:
                new_booking = form.save(commit=False)
                new_booking.user = request.user
                new_booking.save()
                return redirect(reverse('booking_detail', args=[new_booking.id]))
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
