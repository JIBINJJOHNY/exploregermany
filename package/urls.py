from django.urls import path
from . import views


urlpatterns = [
    path('', views.PackageListView.as_view(), name='package-list'),
    path('<int:pk>/', views.PackageDetailView.as_view(), name='package-detail'),
    path('bookings/create/<int:package_id>/', views.booking_create, name='booking_create'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/select-package/', views.select_package, name='select_package'),
    path('booking/form/', views.booking_form, name='booking_form'),

]

 

