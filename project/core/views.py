from django.shortcuts import render
from django.core.paginator import Paginator
from pages.utils.mongodb import get_mongodb_connection
from datetime import datetime
from pages.models import MaklerHouse, FkHouse, LyyskiHouse
from django.db.models import Q
import re

def index(request):

    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    page_number = request.GET.get('page', 1)  # Get the page number from the request
    sort_option = request.GET.get('sort')

    # Create individual querysets for each house type
    makler_markets = MaklerHouse.objects.order_by('-date_added')
    fk_markets = FkHouse.objects.order_by('-date_added')
    lyyski_markets = LyyskiHouse.objects.order_by('-date_added')

    # Apply query and price filters to each queryset
    if query:
        keywords = query.split()
        query_filter = Q()

        for keyword in keywords:
            query_filter |= Q(name__icontains=keyword)

        makler_markets = makler_markets.filter(query_filter)
        fk_markets = fk_markets.filter(query_filter)
        lyyski_markets = lyyski_markets.filter(query_filter)

    if max_price:
        max_price_int = int(max_price)
        makler_markets = makler_markets.filter(price__lte=max_price_int)
        fk_markets = fk_markets.filter(price__lte=max_price_int)
        lyyski_markets = lyyski_markets.filter(price__lte=max_price_int)

    if min_price:
        min_price_int = int(min_price)
        makler_markets = makler_markets.filter(price__gte=min_price_int)
        fk_markets = fk_markets.filter(price__gte=min_price_int)
        lyyski_markets = lyyski_markets.filter(price__gte=min_price_int)

    # Combine querysets for pagination
    combined_markets = list(makler_markets) + list(fk_markets) + list(lyyski_markets)
    
    if sort_option == 'highest_price':
        combined_markets.sort(key=lambda x: x.price if x.price is not None else float('-inf'), reverse=True)
    elif sort_option == 'lowest_price':
        combined_markets.sort(key=lambda x: x.price if x.price is not None else float('inf'))

    # Paginate the combined queryset
    per_page = 10  # Number of items per page
    paginator = Paginator(combined_markets, per_page)
    page_obj = paginator.get_page(page_number)
    

    houses = {
        'query': query,
        'max_price': max_price,
        'min_price': min_price,
        'page_obj': page_obj,
    }



 
#! ANALYTICS DAta

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


    context = { 'avg_price': avg_price_fields, 
                'avg_floor_price': avg_floor_price_fields,  
                'houses': houses,}


    return render(request, 'core/index.html', context)
