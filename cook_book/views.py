from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def update_recipe_view(request, id):
    recipe_id = get_object_or_404(models.Recipes, id=id)
    if request.method == 'POST':
        form = forms.CookBookForm(request.POST, instance=recipe_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно изменен в БД </h1> <a href="/"> Все рецепты:</a>')
    else:
        form = forms.CookBookForm(instance=recipe_id)
        return render(request, template_name='recipes/update_recipe.html',
                    context={'form': form, 'recipe_id': recipe_id})


def delete_recipe_view(request, id):
    recipe_id = get_object_or_404(models.Recipes, id=id)
    recipe_id.delete()
    return HttpResponse('<h1>Успешно удален из БД </h1> <a href="/"> Все рецепты:</a>')


def create_recipe_view(request):
    if request.method == 'POST':
        form = forms.CookBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно добавлен в БД </h1> <a href="/"> Все рецепты:</a>')
    else:
        form = forms.CookBookForm()
    return render(request=request,template_name='recipes/create_recipe.html',
                    context={'form': form})


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

