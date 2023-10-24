from django.urls import path
from . import views


urlpatterns = [
    path('', views.PackageListView.as_view(), name='package-list'),
    path('<int:pk>/', views.PackageDetailView.as_view(), name='package-detail'),
    path('bookings/create/<int:package_id>/', views.booking_create, name='booking_create'),

]

 

