from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField 


# Create your models here.
class State(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='State Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        verbose_name='State Description',
        help_text='Required'
    )
    image = CloudinaryField(
        'state_image',
        folder='state_images/',
        null=True,
        blank=True,
    )
    alt = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Alt text',
        help_text='Optional. Max length: 300 characters'
    )


    def __str__(self):
        return self.name

class TouristPlace(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Destination Name',
        help_text='Required. Max length: 100 characters'
    )
    description = models.TextField(
        verbose_name='Destination Description',
        help_text='Required'
    )
    location = models.CharField(
        max_length=100,
        verbose_name='Destination Location',
        help_text='Required. Max length: 100 characters'
    )
    state = models.ForeignKey(
        State,  # Establish a ForeignKey relationship with the State model
        on_delete=models.CASCADE,  # Define the behavior on State deletion
        verbose_name='State',
        help_text='Required. Max length: 100 characters'
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Tourist Place Slug',
        help_text='Required. Max length: 150 characters'
    )
    google_map_src = models.CharField(
        max_length=500, 
        blank=True, 
        null=True
    )
    

    class Meta:
        verbose_name = 'Tourist Place'
        verbose_name_plural = 'Tourist Places'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

