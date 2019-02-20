from django import forms
from django.forms import ModelForm
from django import forms
from .models import Stuff, City, SubCategory


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(label='Город', queryset=City.objects.all())
    stuff_subcategory = forms.ModelChoiceField(label='Категория', queryset=SubCategory.objects.all())
    data_start = forms.DateField(label='Дата от')
    data_finish = forms.DateField(label='до')
    price_start = forms.DateField(label='Цена от')
    price_finish = forms.DateField(label='до')
    tags = forms.CharField(label='Тэги')