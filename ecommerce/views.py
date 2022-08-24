from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View,UpdateView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
        context['cat'] = Category.objects.get(title='Men')
        return context

class WomanView(TemplateView):
    template_name ='woman_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        context['cat'] = Category.objects.get(title='Women')
        return context

class ChildrenView(TemplateView):
    template_name = 'children_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        context['cat'] = Category.objects.get(title='Childern')
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

class ProductDetailView(TemplateView):
    template_name = 'product_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        context['product'] = Product.objects.get(id=self.kwargs['id'])
        return context


class ClientRegisterView(CreateView):
   template_name='client_register.html'
   form_class = ClientRegisterForm
   success_url = '/'
   def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username,email,password)
        form.instance.user = user
        login(self.request,user)
        return super().form_valid(form)

class ClientLoginView(FormView):
    template_name = 'client_login.html'
    form_class = ClientLoginForm
    success_url = '/'
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request,username=username,password=password)
        if user is not None and Clients.objects.filter(user=user).exists():
            login(self.request,user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)  

class ClientLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class ClientProfileView(TemplateView):
    template_name = 'client_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client']   = Clients.objects.get(user=self.request.user)
        context['shoppies']        = Shoppy.objects.latest('id')
        return context

class UpdateProfileView(UpdateView):
    model = Clients
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'

    def get_object(self,*args,**kwargs):
        client = get_object_or_404(Clients, pk=self.kwargs['id'])
        return client

    def get_success_url(self):
        success_url = reverse_lazy('ecommerce:client_profile')
        return success_url
