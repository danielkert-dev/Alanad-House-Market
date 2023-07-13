from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MaklerHouse

# Create your views here.

def maklar(request):
    houses = MaklerHouse.objects.all()

    
    paginator = Paginator(houses, 10)  # Set the number of houses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'house_maklar/maklar.html' , {'page_obj': page_obj})