from django.urls import path
from . import views


urlpatterns = [
    path('', views.PackageListView.as_view(), name='home'),
 
]
