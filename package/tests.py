from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import State, Package, Booking  
from .forms import BookingForm

class PackageViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.state = State.objects.create(name='Test State', description='Test State Description')
        self.package = Package.objects.create(
            name='Test Package',
            description='Test Package Description',
            state=self.state,
            price=100.00
        )

    def test_package_list_view(self):
        response = self.client.get(reverse('package-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['states'], ['<State: Test State>'])
        self.assertQuerysetEqual(response.context['packages'], ['<Package: Test Package>'])

    def test_package_detail_view(self):
        response = self.client.get(reverse('package-detail', args=[self.package.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['package'], self.package)

    def test_booking_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('booking_create', args=[self.package.id]))
        self.assertEqual(response.status_code, 200)



    def test_book_now_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('book_now', args=[self.package.id]))
        self.assertEqual(response.status_code, 200)


class BookingFormTests(TestCase):
    def test_valid_booking_form(self):
        form = BookingForm(data={
            'date': '2023-12-31',
            'no_of_guests': 4,
            'contact_email': 'test@example.com',
            'contact_phone': '1234567890',
            'special_requests': 'None',
            'payment_amount': 100.00,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form(self):
        form = BookingForm(data={})  
        self.assertFalse(form.is_valid())
