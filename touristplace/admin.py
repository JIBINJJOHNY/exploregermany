from django.contrib import admin
from .models import State,TouristPlace,TouristPlaceImage,Review

admin.site.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(TouristPlace, TouristPlaceAdmin)
class TouristPlaceAdmin(admin.ModelAdmin):
    inlines = [TouristPlaceImageInline]
    list_display = ('name', 'location', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'location', 'state')

class TouristPlaceImageInline(admin.TabularInline):
    model = TouristPlaceImage
    extra = 1  # Number of empty image forms to display

admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'tourist_place', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__username', 'tourist_place__name')

