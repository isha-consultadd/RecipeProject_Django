from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def recipes(request):

    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe-image')
        recipe_name = data.get('recipe-name')
        recipe_description = data.get('recipe-description')
        
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,

        )
        return redirect('/')
    recipes = Recipe.objects.all()
    return render(request , 'rec/recipes.html' , {'recipes':recipes})

def delete_recipes(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def update_recipes(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe-image')
        recipe_name = data.get('recipe-name')
        recipe_description = data.get('recipe-description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if queryset.recipe_image:
             queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/')
    context = {"recipes":queryset}
    return render(request , 'rec/update-recipe.html' , context)
