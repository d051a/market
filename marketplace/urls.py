from django.contrib import admin
from django.urls import path, re_path

from .views import StuffList

urlpatterns = [
    path('', StuffList.as_view(), name='home'),
    re_path(r'^search/', StuffList.as_view(), name='search_page'),
]