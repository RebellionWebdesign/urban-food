from django.shortcuts import render
from django.views import View
from .models import Meal


class MealViewHome(View):
    model = Meal
    queryset = Meal.objects.filter.all()
    template_name = 'index.html'

class MealViewMenu(View):
    model = Meal
    queryset = Meal.objects.filter.all()
    template_name = 'menu.html'
