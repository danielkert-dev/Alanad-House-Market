from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path("maklar/", views.maklar, name="maklar"),
    path("fk/", views.fk, name="fk"),
]