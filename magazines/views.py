from django.shortcuts import render
from .models import Magazine
# Create your views here.


def all_magazine(request):
    magazine = Magazine.objects.all()
    return render(request, "magazine/magazine.html", {"magazine": magazine})

from django.shortcuts import render

# Create your views here.
