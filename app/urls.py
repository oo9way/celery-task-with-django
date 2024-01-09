from app.views import get_random_images
from django.urls import path

urlpatterns = [path("", get_random_images)]
