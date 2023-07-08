from django.shortcuts import render
from django.utils import translation


def index(request):
    return render(request, 'core/index.html')
