from apps.sklad.views import *
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
app_name = 'sklad'
urlpatterns = [
    path('', StartSkladView.as_view(), name = 'start'),
    path('<int:id>/formaauto', StartSkladView.forma, name = 'formaauto'),
    path('/addagent', StartSkladView.addAgent, name = 'addagent'),
]
