from django.shortcuts import render
# from django.utils import translation
from pages.models import AveragePrice

def index(request):

    average_prices = AveragePrice.objects.all()

    return render(request, 'core/index.html', {'average_prices': average_prices})
