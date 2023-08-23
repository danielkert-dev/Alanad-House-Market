from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import MaklerHouse, LyyskiHouse, FkHouse

from .forms import FormHouseForm
from .utils.mongodb import get_mongodb_connection
from datetime import datetime

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


#! ANALYTICS 
def analytics(request):

    db_name_avg_price = 'average_price'
    db_avg_price = get_mongodb_connection(db_name_avg_price)
    collection_avg_price = db_avg_price[f"data_{datetime.now().strftime('%Y-%m-%d')}"]

    # Get the first document from the collection
    avg_price = collection_avg_price.find_one()

    # Extract specific fields excluding '_id'
    if avg_price:
        avg_price_fields = {
            'date': avg_price['date'],
            'average_price_maklar': avg_price['average_price_maklar'],
            'average_price_fk': avg_price['average_price_fk'],
            'average_price_lyyski': avg_price['average_price_lyyski'],
            'overall_average_price': avg_price['overall_average_price']
        }
    else:
        avg_price_fields = None


    db_name_avg_floor_price = 'average_floor_price'
    db_avg_floor_price = get_mongodb_connection(db_name_avg_floor_price)
    collection_avg_floor_price = db_avg_floor_price[f"data_{datetime.now().strftime('%Y-%m-%d')}"]

    # Get the first document from the collection
    avg_floor_price = collection_avg_floor_price.find_one()

    # Extract specific fields excluding '_id'
    if avg_floor_price:
        avg_floor_price_fields = {
            'date': avg_floor_price['date'],
            'average_cost_per_area_maklar': avg_floor_price['average_cost_per_area_maklar'],
            'average_cost_per_area_fk': avg_floor_price['average_cost_per_area_fk'],
            'average_cost_per_area_lyyski': avg_floor_price['average_cost_per_area_lyyski'],
            'overall_average_cost_per_area': avg_floor_price['overall_average_cost_per_area']
        }
    else:
        avg_floor_price_fields = None


    avg_municipality_price_db_name = 'average_municipality_price'
    avg_municipality_price_db = get_mongodb_connection(avg_municipality_price_db_name)
    avg_municipality_price_collection = avg_municipality_price_db[f"data_{datetime.now().strftime('%Y-%m-%d')}"]

    # Get the first document from the collection
    avg_municipality_price_document = avg_municipality_price_collection.find_one()

    # Extract specific fields excluding '_id'
    if avg_municipality_price_document:
        avg_municipality_price_fields = {
            'date': avg_municipality_price_document['date'],
            'average_price_maklar': avg_municipality_price_document['average_price_maklar_municipality'],
            'average_price_fk': avg_municipality_price_document['average_price_fk_municipality'],
            'average_price_lyyski': avg_municipality_price_document['average_price_lyyski_municipality'],
            'overall_average_price': avg_municipality_price_document['overall_average_price_municipality']
        }
    else:
        avg_municipality_price_fields = None



    context = {'avg_price': avg_price_fields, 'avg_floor_price': avg_floor_price_fields,  'avg_municipality_price': avg_municipality_price_fields,}

    return render(request, 'pages/analytics.html', context)
