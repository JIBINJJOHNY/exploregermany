from django.urls import path, include
from . import views
from .views import delete_review 
urlpatterns = [
    path('', views.home, name='home'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('state_detail/<int:state_id>/', views.state_detail, name='state_detail'),
    path('place/<int:place_id>/', views.place_details, name='place_details'),
    path('get_large_image/<int:image_id>/', views.get_large_image, name='get_large_image'),
    path('add_review/<int:tourist_place_id>/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('view_review/<int:tourist_place_id>/reviews/', views.view_reviews, name='view_review'),
    path('delete_review/<int:tourist_place_id>/<int:review_id>/', delete_review, name='delete_review'),
    path('account/delete/', views.account_delete, name='account_delete'),

]