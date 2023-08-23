# forms.py
from django import forms
from pages.models import MaklerHouse, FkHouse, LyyskiHouse

class HouseSearchForm(forms.Form):
    search_query = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)