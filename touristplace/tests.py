from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import State, TouristPlace

class TouristPlaceTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a state
        self.state = State.objects.create(
            name='Test State',
            description='Test State Description'
        )

        # Create a tourist place
        self.tourist_place = TouristPlace.objects.create(
            name='Test Place',
            description='Test Place Description',
            location='Test Location',
            state=self.state,
            slug='test-place'
        )

    def test_place_detail_view(self):
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

        # Access the place detail view
        response = self.client.get(reverse('place_details', args=[self.tourist_place.id]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the place's name
        self.assertContains(response, 'Test Place')

    def test_add_review_view(self):
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

        # Access the add review view
        response = self.client.get(reverse('add_review', args=[self.tourist_place.id]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the form
        self.assertContains(response, '<form')

    def test_edit_review_view(self):
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

        # Create a review
        review = Review.objects.create(
            user=self.user,
            tourist_place=self.tourist_place,
            rating=5
        )

        # Access the edit review view
        response = self.client.get(reverse('edit_review', args=[review.id]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the form
        self.assertContains(response, '<form')

    def test_view_reviews_view(self):
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

        # Access the view reviews view
        response = self.client.get(reverse('view_review', args=[self.tourist_place.id]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the place's name
        self.assertContains(response, 'Test Place')
