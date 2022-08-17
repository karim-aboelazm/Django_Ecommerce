from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomeView(TemplateView):
    template_name = 'home_page.html'
    
class MenView(TemplateView):
    template_name = 'men_page.html'

class WomanView(TemplateView):
    template_name ='woman_page.html'

class ChildrenView(TemplateView):
    template_name = 'children_page.html'

class CategoryView(TemplateView):
    template_name = 'categories_page.html'
