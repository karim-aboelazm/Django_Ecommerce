from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View,UpdateView
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ecommerce.utils import password_reset_token
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
        context['available_languages'] = ['en','ar']
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

class ForgotPasswordView(FormView):
    template_name = 'forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = '/forget-password/?m=s'
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        url = self.request.META['HTTP_HOST']
        client = Clients.objects.get(user__email=email)
        user = client.user
        text_content = f'Hi, {client.full_name} ! You have requested a password reset for your account at {email}. Please go to the following page and add a new password.\n'
        html_content = "http://"+ url + "/reset-password/" + email+ "/" +password_reset_token.make_token(user)+"/"
        send_mail(
            'Password Reset Link | Shoppy E-commerce',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        print(html_content)
        return super().form_valid(form)

class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
    form_class = PasswordResetForm
    success_url = '/client-login/'
    def form_valid(self, form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get('email')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class AddToCartView(TemplateView):
    template_name = 'add_to_cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        product = Product.objects.get(id=self.kwargs['id'])
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart.cartproduct_set.filter(product=product)
            if this_product_in_cart.exists():
                cart_product = this_product_in_cart.last()
                cart_product.quantity += 1
                cart_product.subtotal += product.price
                cart_product.save()
                cart.total += product.price
                cart.save()
            else:
                cart_product = CartProduct.objects.create(cart=cart,product=product,rate=product.price,quantity=1,subtotal=product.price)
                cart.total += product.price
                cart.save()
        else:
            cart = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart.id
            cart_product = CartProduct.objects.create(cart=cart,product=product,rate=product.price,quantity=1,subtotal=product.price)
            cart.total += product.price
            cart.save()      
        return context

class CartView(TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context

class ManageCartView(View):
    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')
        cp = CartProduct.objects.get(id=self.kwargs['id'])
        cart = cp.cart
        if action == 'inc':
            cp.quantity += 1
            cp.subtotal += cp.rate
            cp.save()
            cart.total += cp.rate
            cart.save()
        elif action == 'dcr':
            cp.quantity -= 1
            cp.subtotal -= cp.rate
            cp.save()
            cart.total -= cp.rate
            cart.save()
            if cp.quantity == 0:
                cp.delete()
        elif action == 'rmv':
            cart.total -= cp.subtotal
            cart.save()
            cp.delete()
        else:
            pass
        return redirect('ecommerce:cart')

class EmptyCartView(View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('ecommerce:cart')

class CheckoutView(CreateView):
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppies'] = Shoppy.objects.latest('id')
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            form.instance.cart = cart
            form.instance.subtotal = cart.total
            form.instance.discount = 0
            form.instance.total = cart.total
            form.instance.order_status = 'Order Received'
            del self.request.session['cart_id']
            payment_method = form.cleaned_data.get('payment_method')
            order = form.save()
            if payment_method == 'Paypal':
                return redirect(reverse('ecommerce:payment')+"?o_id="+str(order.id))

            elif payment_method == 'Master Card' :
                return redirect(reverse('ecommerce:payment')+"?o_id="+str(order.id))

            elif payment_method == 'Visa Card':
                return redirect(reverse('ecommerce:payment')+"?o_id="+str(order.id))
            else:
                pass
        else:
            return redirect('ecommerce:home')
        return super().form_valid(form)

class PaypalAndBankView(View):
    def get(self,request, *args, **kwargs):
        order_id = request.GET.get('o_id')
        context = {}
        context['shoppies'] = Shoppy.objects.latest('id')
        context['order'] = Order.objects.get(id=order_id)
        return render(request, 'paypal_and_bank.html', context)