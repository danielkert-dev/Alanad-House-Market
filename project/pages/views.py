from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import MaklerHouse
from .models import FkHouse

# Create your views here.

@login_required
def maklar(request):
    houses = MaklerHouse.objects.all()

    
    paginator = Paginator(houses, 10)  # Set the number of houses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/maklar.html' , {'page_obj': page_obj})

@login_required
def fk(request):
    houses = FkHouse.objects.all()

    paginator = Paginator(houses, 10)  # Set the number of houses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/fk.html' , {'page_obj': page_obj})