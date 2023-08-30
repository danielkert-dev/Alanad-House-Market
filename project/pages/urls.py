from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path("maklar/", views.maklar, name="maklar"),
    path("fk/", views.fk, name="fk"),
    path("lyyski/", views.lyyski, name="lyyski"),
    path("analytics/", views.analytics, name="analytics"),
    path('form/', views.create_form_house, name='form'),
    path('page/', views.page, name='page'),
]
