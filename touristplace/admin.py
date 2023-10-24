from django.contrib import admin
from .models import State, TouristPlace, TouristPlaceImage, Review

# Define the StateAdmin class
class StateAdmin(admin.ModelAdmin):
    # Configure how the State model is displayed in the admin interface
    list_display = ('name', 'description', 'alt')
    search_fields = ('name', 'description', 'alt')
    list_filter = ('name',)

# Define an inline model for TouristPlaceImage
class TouristPlaceImageInline(admin.TabularInline):
    model = TouristPlaceImage
    extra = 1  # Number of empty image forms to display

# Configure how the TouristPlace model is displayed in the admin interface
class TouristPlaceAdmin(admin.ModelAdmin):
    inlines = [TouristPlaceImageInline]
    list_display = ('name', 'location', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'location', 'state')

# Configure how the Review model is displayed in the admin interface
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'tourist_place', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__username', 'tourist_place__name')


# Register the State model with the StateAdmin class
admin.site.register(State)

# Register the TouristPlace model with the TouristPlaceAdmin class
admin.site.register(TouristPlace, TouristPlaceAdmin)

# Register the Review model with the ReviewAdmin class
admin.site.register(Review, ReviewAdmin)