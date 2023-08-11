from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import MaklerHouse, LyyskiHouse, FkHouse, AveragePrice

from .forms import FormHouseForm

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

@login_required
def lyyski(request):
    houses = LyyskiHouse.objects.all()

    paginator = Paginator(houses, 10)  # Set the number of houses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/lyyski.html' , {'page_obj': page_obj})

def analytics(request):

    average_prices = AveragePrice.objects.all()

    return render(request, 'pages/analytics.html', {'average_prices': average_prices})


def create_form_house(request):
    if request.method == 'POST':
        form = FormHouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form saved successfully!')
            return redirect('core:index')  # Redirect to a relevant page
        else:
            messages.warning(request, 'Form did not save due to errors. Please check your input.')
    else:
        form = FormHouseForm()
    
    return render(request, 'pages/form.html', {'form': form})
