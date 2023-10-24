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
