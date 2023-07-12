from django.urls import path

from . import views

app_name = 'maklar'

urlpatterns = [
    path("maklar/", views.maklar, name="maklar"),
]