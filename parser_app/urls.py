from django.urls import path
from . import views

urlpatterns = [
    path('food_list/', views.ParserListFood.as_view(), name='food_list'),
    path('start_parser/', views.GetParsingForm.as_view(), name='start_parser'),
]