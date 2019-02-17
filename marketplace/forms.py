from django import forms
from django.forms import ModelForm
from .models import Stuff


class SearchForm(ModelForm):
    class Meta:
        model = Stuff
        fields = ['city', 'stuff_subcategory', 'tags', ]