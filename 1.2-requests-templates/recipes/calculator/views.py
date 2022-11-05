from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def calc(ingredients, servings):
    ingr = {}
    for ingredient, number in ingredients.items():
        number *= servings
        ingr[ingredient] = round(number, 1)
    return ingr


def omlet(request):
    ingredients = DATA.get('omlet')
    servings = int(request.GET.get("servings", 1))
    context = {'recipe': calc(ingredients, servings)}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    ingredients = DATA.get('pasta')
    servings = int(request.GET.get("servings", 1))
    context = {'recipe': calc(ingredients, servings)}
    return render(request, 'calculator/index.html', context)

def buter(request):
    ingredients = DATA.get('buter')
    servings = int(request.GET.get("servings", 1))
    context = {'recipe': calc(ingredients, servings)}
    return render(request, 'calculator/index.html', context)

