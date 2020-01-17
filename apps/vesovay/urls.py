from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.vesovay.views import *

app_name = 'vesovay'
urlpatterns = [
    path('', StartVesView.as_view(), name= 'start'),
    path('<int:error>/<nomer>/', StartVesView.by_error, name= 'by_erorr'),
    path('/addCar', AddVesCarView.as_view(), name='addcar')
]
