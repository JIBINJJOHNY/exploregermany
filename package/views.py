from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import State
from .models import Package,Booking
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse
from .forms import BookingForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import never_cache
import smtplib
import ssl
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
    state = package.state

    if request.method == 'POST':
        messages1 = ''
        form = BookingForm(request.POST)
        if form.is_valid():
            # Check if the date is in the past and restrict it to the future
            booking_date = form.cleaned_data['date']
            if booking_date < timezone.now().date():
                message_alert="Booking date must be from the current date onward"
                messages1.append(message_alert)
                request.session['messages1']= messages1
                print('alert')
                form.add_error('date', ValidationError('Booking date must be from the current date onward'))
                return render(request, 'booking_form.html', {'form': form,'state': state ,'alert_message':alert_message})
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

    return render(request, 'booking_form.html', {'form': form,'state': state})

@login_required
def booking_detail(request, booking_id):
    # View to display the details of a single booking
    booking = get_object_or_404(Booking, pk=booking_id)
    state = booking.package.state 
    return render(request, 'booking_detail.html', {'booking': booking,'state': state})

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
@never_cache
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


@csrf_protect
def book_now(request, booking_id):
    # Assuming you are passing the booking ID as an argument in the URL
    booking = Booking.objects.get(id=booking_id)
    alert_message = ""
    
    if request.method == 'POST':
        # Get the user's email from the booking object
        user_email = booking.contact_email
        
        # Create an SSL context using the system's CA certificates
        context = ssl.create_default_context()

        # Your SMTP server settings should be configured in settings.py
        smtp_server = settings.EMAIL_HOST
        smtp_port = settings.EMAIL_PORT
        from_email = settings.EMAIL_HOST_USER
        email_password = settings.EMAIL_HOST_PASSWORD  # You may want to use a safer method to store the password

        # Compose the email message
        subject = "Booking Confirmation"
        recipient_list = [user_email]

        # Get the user's full name by calling the get_full_name method
        user_full_name = booking.user.get_full_name()

        # Compose the email message including booking details
        message = f"Thank you for choosing the 'Cash' payment option. We value your booking!\n\nBooking Details:\n"
        message += f"User: {user_full_name}\n"
        message += f"Booking Date: {booking.date}\n"
        message += f"Number of Guests: {booking.no_of_guests}\n"
        message += f"Package: {booking.package}\n"
        message += f"Email: {booking.contact_email}\n"
        message += f"Contact Phone: {booking.contact_phone}\n"
        message += f"Special Requests: {booking.special_requests}\n"
        message += f"Payment Amount: €{booking.payment_amount}\n"
        message += "\nTo confirm your reservation, please contact us at your earliest convenience."
        message += "Our team is here to assist you and ensure your booking is smooth and enjoyable."
        message += "You can reach us via email at support@exploredeutschland.com or by phone at +49 1523 456 7890."
        message += "We look forward to helping you with your booking details and any special requests you may have."

        try:
            print("Before sending the email")
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            print("After sending the email")
            alert_message = "Booking successful. Check your email for confirmation."
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            return HttpResponse("An error occurred while booking.")
    
    return render(request, 'booking_detail.html', {'booking': booking, 'alert_message': alert_message})
    
