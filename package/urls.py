from django.urls import path
from . import views


urlpatterns = [
    path('', views.PackageListView.as_view(), name='package-list'),
    path('<int:pk>/', views.PackageDetailView.as_view(), name='package-detail'),

]

 

