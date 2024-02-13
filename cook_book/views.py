from django.shortcuts import render
from . import models


def cookbook_list(request):
    if request.method == 'GET':
        recipes = models.Recipes.objects.all()
        return render(request, 'recipes/recipe_list.html',
                      {'recipes': recipes})
