from django.contrib import admin
from django.urls import path, include
from .views import departs, depart_values,results

app_name = 'core'
urlpatterns = [
    path('', departs, name='home'),
    path('<slug:office_slug>/', depart_values, name='depart_values'),
    path('<slug:office_slug>/', depart_values, name='depart_values'),
    path('<slug:office_slug>/result/', results, name='results')
]