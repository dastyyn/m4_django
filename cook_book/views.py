from django.shortcuts import render, get_object_or_404
from . import models


def cookbook_list(request):
    if request.method == 'GET':
        recipes = models.Recipes.objects.all()
        return render(request, 'recipes/recipe_list.html',
                      {'recipes': recipes})


def cookbook_detail_view(request, id):
    if request.method == 'GET':
        recipe_id = get_object_or_404(models.Recipes, id=id)
        return render(request, 'recipes/recipe_detail.html',
                      context={'recipe_id': recipe_id})


