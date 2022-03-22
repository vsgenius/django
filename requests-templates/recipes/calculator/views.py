from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'colbasa':{
        'bumaga':5,
        'myaso':1,
        'jir':1
    }
    # можете добавить свои рецепты ;)
}


def index(request):
    return HttpResponse('Рецепты')


def recipes(request, recipe):
    new_data = {}
    count = int(request.GET.get('servings', 1))
    if recipe in DATA:
        for key, val in DATA[recipe].items():
            new_data[key] = val*count
    context = {'recipe': new_data}
    return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
