from django.urls import path
from . import views

urlpatterns = [
    path('', views.cookbook_list, name='cookbook_list'),
    path('recipe_detail/<int:id>/', views.cookbook_detail_view, name='recipe_detail'),
]
