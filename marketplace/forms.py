from django import forms
from .models import City, SubCategory


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Название, описание'}), required=False)
    city = forms.ModelChoiceField(label='Город', queryset=City.objects.all(), required=False)
    stuff_subcategory = forms.ModelChoiceField(label='Категория', queryset=SubCategory.objects.all(), required=False)
    data_start = forms.DateField(label='Дата от', required=False)
    data_finish = forms.DateField(label='Дата до', required=False)
    price_start = forms.IntegerField(label='Цена от', required=False)
    price_finish = forms.IntegerField(label='Цена до', required=False)
    tags = forms.CharField(label='Тэги', required=False)
