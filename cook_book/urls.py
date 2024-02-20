from django.urls import path
from . import views

urlpatterns = [
    path('', views.cookbook_list, name='cookbook_list'),
    path('recipe_detail/<int:id>/', views.cookbook_detail_view, name='recipe_detail'),
    path('recipe_detail/<int:id>/delete/', views.delete_recipe_view , name='recipe_delete'),
    path('recipe_detail/<int:id>/update/', views.update_recipe_view , name='recipe_update'),
    path('create_recipe/', views.create_recipe_view, name='create_recipe'),
]
