from django import forms
from .models import FormHouse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


class FormHouseForm(forms.ModelForm):
    class Meta:
        model = FormHouse
        exclude = ['id']
        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.URLInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'low_img': forms.URLInput(attrs={'class': 'form-control'}),
            'high_img': forms.URLInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'plot_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'municipality': forms.TextInput(attrs={'class': 'form-control'}),
            'costs': forms.NumberInput(attrs={'class': 'form-control'}),
            'vr_img': forms.URLInput(attrs={'class': 'form-control'}),
            
            # Repeat the above lines for other fields
        }
