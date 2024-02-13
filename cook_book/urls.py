from django.urls import path
from . import views

urlpatterns = [
    path('', views.cookbook_list, name='cookbook_list'),
]
