from django.urls import path
from . import views

urlpatterns = [
    path("", views.post, name='post'),
    path("<str:id>/", views.postdetails, name='post_details'),
]