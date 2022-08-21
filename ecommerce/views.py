from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.core.paginator import Paginator
from .models import *
from .forms import *

class HomeView(CreateView):
    template_name = 'home_page.html'
    form_class = SubscribeForm
    success_url = '/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        return super(HomeView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        context['sliders'] = Slider.objects.all()
        context['offers'] = Offer.objects.latest('id')
        context['products'] = Product.objects.all().order_by('-id')
        context['about_company'] = About_Company.objects.all().order_by('-id')
        return context

    
class MenView(TemplateView):
    template_name = 'men_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        return context

class WomanView(TemplateView):
    template_name ='woman_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        return context

class ChildrenView(TemplateView):
    template_name = 'children_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        return context

class AllProductsView(TemplateView):
    template_name = 'allproducts_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        all_products = Product.objects.all().order_by('-id')
        paginator = Paginator(all_products,8)
        page_number = self.request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context['products'] = product_list
        return context
