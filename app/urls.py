import imp
from django.urls import path
from .views import csv_file_api

urlpatterns = [
    path("api/csvsync/", csv_file_api, name="csv_sync_api")
]