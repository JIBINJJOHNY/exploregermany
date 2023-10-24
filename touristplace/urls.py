from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('state_detail/<int:state_id>/', views.state_detail, name='state_detail'),
    path('place/<int:place_id>/', views.place_details, name='place_details'),
]