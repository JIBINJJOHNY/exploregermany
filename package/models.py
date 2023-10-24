from django.db import models
from touristplace.models import TouristPlace,State  # Adjust the import path as needed
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Package(models.Model):
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name='State',
        help_text='Choose the state for this package'
    )
    package_type = models.CharField(
        max_length=10,
        choices=[('1', '1 Day'), ('2', '2 Days')],
        verbose_name='Package Type',
        help_text='Select the package type (1 Day or 2 Days)'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price',
        help_text='Enter the price for this package'
    )
    PLACES_LIMIT_CHOICES = (
        (1, '3 Places (1 Day)'),
        (2, '6 Places (2 Days)'),
    )

    places_limit = models.IntegerField(
        choices=PLACES_LIMIT_CHOICES,
        verbose_name='Places Limit',
        help_text='Select the limit for tourist places'
    )

    def get_places_limit_display(self):
        for limit, limit_display in self.PLACES_LIMIT_CHOICES:
            if limit == self.places_limit:
                return limit_display
        return None  # Handle the case where places_limit doesn't match any choice
    def get_description(self):
        if self.package_type == '1':
            return f" Discover the beauty of {self.state.name} with our exclusive 1-day package. Enjoy a comfortable journey in a luxurious Mercedes-Benz vehicle, as we take you on an adventure to explore the most enchanting tourist places in the area. The best part? There are no additional entrance fees, so you can visit all the attractions without any extra cost. Please note that this package does not include food expenses, so you'll have the freedom to choose your own dining options along the way. Experience the joy of exploration and create lasting memories on this exciting day trip!"
        elif self.package_type == '2':
            return f"Discover the beauty of {self.state.name} with our exclusive 2-day package. Enjoy a comfortable journey in a luxurious Mercedes-Benz vehicle, as we take you on an adventure to explore the most enchanting tourist places in the area. The best part? There are no additional entrance fees, so you can visit all the attractions without any extra cost. As part of this package, we offer you a premium 4-star hotel accommodation for one night, ensuring a restful and rejuvenating stay. Our top priority is your comfort and relaxation, and we've chosen the finest accommodation to make your trip memorable. Please note that this package does not include food expenses, so you'll have the freedom to choose your own dining options along the way. Experience the joy of exploration and create lasting memories on this exciting 2-day trip!"
        else:
            return ""

    places = models.ManyToManyField(
        'touristplace.TouristPlace',  # Use a lazy reference to avoid circular import
        verbose_name='Tourist Places',
        help_text='Select tourist places for this package'
    )

    def __str__(self):
        return f'Package for {self.state.name} - {self.get_package_type_display()}'
    
