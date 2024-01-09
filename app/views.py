from django.shortcuts import render
from app.tasks import download_images


# Create your views here.
def get_random_images(request):
    if request.method == "POST":
        download_images.delay()
    return render(request, "app/index.html")
