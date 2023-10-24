from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('state_detail/<int:state_id>/', views.state_detail, name='state_detail'),
]