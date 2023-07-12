from django.shortcuts import render
from .models import MaklerHouse

# Create your views here.

def maklar(request):
    houses = MaklerHouse.objects.all()

    return render(request, 'house_maklar/maklar.html' , {'houses': houses})