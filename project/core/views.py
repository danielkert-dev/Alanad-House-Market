from django.shortcuts import render
from django.core.paginator import Paginator
from pages.utils.mongodb import get_mongodb_connection
from datetime import datetime
from pages.models import MaklerHouse, FkHouse, LyyskiHouse, AktiaHouse, MapData
from django.db.models import Q
import re
from urllib.parse import urlparse

def index(request):

    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    page_number = request.GET.get('page', 1)  # Get the page number from the request
    sort_option = request.GET.get('sort')
    selected_municipality = request.GET.get('municipality')
    selected_type = request.GET.get('type')


    # Create individual querysets for each house type
    makler_markets = MaklerHouse.objects.order_by('-date_added')
    fk_markets = FkHouse.objects.order_by('-date_added')
    lyyski_markets = LyyskiHouse.objects.order_by('-date_added')
    aktia_markets = AktiaHouse.objects.order_by('-date_added')

    # Get unique municipalities from all house types
    unique_municipalities = set()
    unique_municipalities.update(makler_markets.values_list('municipality', flat=True))
    unique_municipalities.update(fk_markets.values_list('municipality', flat=True))
    unique_municipalities.update(lyyski_markets.values_list('municipality', flat=True))
    unique_municipalities.update(aktia_markets.values_list('municipality', flat=True))

    # Get unique types from all house types
    unique_types = set()
    unique_types.update(makler_markets.values_list('type', flat=True))
    unique_types.update(fk_markets.values_list('type', flat=True))
    unique_types.update(lyyski_markets.values_list('type', flat=True))
    unique_types.update(aktia_markets.values_list('type', flat=True))

    # Filter out None values and sort
    municipalities = sorted(filter(None, unique_municipalities))
    types = sorted(filter(None, unique_types))

    # Apply query and price filters to each queryset
    if query:
        keywords = query.split()
        query_filter = Q()

        for keyword in keywords:
            query_filter |= Q(name__icontains=keyword) | Q( municipality__icontains=keyword) | Q( address__icontains=keyword ) | Q( type__icontains=keyword)

        makler_markets = makler_markets.filter(query_filter)
        fk_markets = fk_markets.filter(query_filter)
        lyyski_markets = lyyski_markets.filter(query_filter)
        aktia_markets = aktia_markets.filter(query_filter)

    if max_price:
        max_price_int = int(max_price)
        makler_markets = makler_markets.filter(price__lte=max_price_int)
        fk_markets = fk_markets.filter(price__lte=max_price_int)
        lyyski_markets = lyyski_markets.filter(price__lte=max_price_int)
        aktia_markets = aktia_markets.filter(price__lte=max_price_int)

    if min_price:
        min_price_int = int(min_price)
        makler_markets = makler_markets.filter(price__gte=min_price_int)
        fk_markets = fk_markets.filter(price__gte=min_price_int)
        lyyski_markets = lyyski_markets.filter(price__gte=min_price_int)
        aktia_markets = aktia_markets.filter(price__gte=min_price_int)

    # Filter based on selected municipality
    if selected_municipality:
        makler_markets = makler_markets.filter(municipality=selected_municipality)
        fk_markets = fk_markets.filter(municipality=selected_municipality)
        lyyski_markets = lyyski_markets.filter(municipality=selected_municipality)
        aktia_markets = aktia_markets.filter(municipality=selected_municipality)

    # Filter based on selected type
    if selected_type:
        makler_markets = makler_markets.filter(type=selected_type)
        fk_markets = fk_markets.filter(type=selected_type)
        lyyski_markets = lyyski_markets.filter(type=selected_type)
        aktia_markets = aktia_markets.filter(type=selected_type)



    # Combine querysets for pagination
    combined_markets = list(makler_markets) + list(fk_markets) + list(lyyski_markets) + list(aktia_markets)
    
    if sort_option == 'highest_price':
        combined_markets.sort(key=lambda x: x.price if x.price is not None else float('-inf'), reverse=True)
    elif sort_option == 'lowest_price':
        combined_markets.sort(key=lambda x: x.price if x.price is not None else float('inf'))

    # Paginate the combined queryset
    per_page = 10  # Number of items per page
    paginator = Paginator(combined_markets, per_page)
    page_obj = paginator.get_page(page_number)

    # Calculate the range of page numbers to display in the paginator
    current_page = page_obj.number
    page_range = range(max(1, current_page - 5), min(current_page + 6, paginator.num_pages + 1))

    

    houses = {
        'query': query,
        'max_price': max_price,
        'min_price': min_price,
        'page_obj': page_obj,
        'municipality': request.GET.get('municipality'),  # Get the municipality from the request for select
        'type': request.GET.get('type'),  # Get the type from the request for select
        'page_range': page_range,  # Add the calculated page range to the houses dictionary

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

    #? Extra data

    # Modify the extraction logic for market names and domains
    for market in combined_markets:
        parsed_url = urlparse(market.link)
        domain_name = parsed_url.netloc.split(':')[0]  # Extract the domain name without port
        market.domain_name = domain_name  # Store the extracted domain name


    # Create a list of links from the combined_markets queryset
    combined_links = [market.link for market in combined_markets]

    # Filter map_data to include only those with links present in the combined_links list
    filtered_map_data = MapData.objects.filter(unique_identifier__in=combined_links)

    # Filter out data points with no address from filtered_map_data
    filtered_map_data = filtered_map_data.exclude(address='No address')

    context = {
        'avg_price': avg_price_fields, 
        'avg_floor_price': avg_floor_price_fields,  
        'houses': houses,
        'combined_markets': combined_markets,
        'municipalities': municipalities,  # Pass the municipalities to the template
        'types': types,  # Pass the types to the template
        'request': request,
        'map_data': filtered_map_data
    }


    return render(request, 'core/index.html', context)

