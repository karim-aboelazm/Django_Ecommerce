from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Shoppy(models.Model):
    icon            = models.ImageField(_('icon'),upload_to="shoppy/")
    title           = models.CharField(_('title'),max_length=50)
    title_ar        = models.CharField(_('title_ar'),max_length=50,blank=True)
    description     = models.TextField(_('description'))
    description_ar  = models.TextField(_('description_ar'),blank=True)
    phone           = models.CharField(_('phone'),max_length=20)
    address         = models.CharField(_('address'),max_length=200)
    address_ar      = models.CharField(_('address_ar'),max_length=200,blank=True)
    fb_link         = models.URLField(_('fb_link'),blank=True, null=True)
    tw_link         = models.URLField(_('tw_link'),blank=True, null=True)
    ins_link        = models.URLField(_('ins_link'),blank=True, null=True)
    li_link         = models.URLField(_('li_link'),blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _('Shoppy')

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(_('email'))
    class Meta:
            verbose_name_plural = _('Subscriber')
    def __str__(self):
        return self.email

class Slider(models.Model):
    image = models.ImageField(_('image'),upload_to="slider/")
    title = models.CharField(_('title'),max_length=250)
    title_ar = models.CharField(_('title_ar'),max_length=250,blank=True)
    class Meta:
        verbose_name_plural = _('Slider')
    def __str__(self):
        return "Slide number : " + str(self.id)
        
class Offer(models.Model):
    title = models.CharField(_('title'),max_length=250)
    title_ar = models.CharField(_('title_ar'),max_length=250,blank=True)
    rate = models.IntegerField(_('rate'),default=0)
    description = models.TextField(_('description'),)
    description_ar = models.TextField(_('description_ar'),blank=True)
    image = models.ImageField(_('image'),upload_to="offer/")
    class Meta:
        verbose_name_plural = _('Offer')
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_('title'),max_length=50)
    title_ar = models.CharField(_('title_ar'),max_length=50,blank=True)
    class Meta:
        verbose_name_plural = _('Category')
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    title_ar = models.CharField(_('title_ar'),max_length=50,blank=True)
    description = models.TextField(_('description'),)
    description_ar = models.TextField(_('description_ar'),blank=True)
    image = models.ImageField(_('image'),upload_to="product/")
    price = models.IntegerField(_('price'),default=0)
    discound = models.IntegerField(_('discound'),default=0)
    policy_return = models.CharField(_('policy_return'),max_length=250,blank=True)
    policy_return_ar = models.CharField(_('policy_return_ar'),max_length=250,blank=True)
    warnty = models.CharField(_('warnty'),max_length=250,blank=True)
    warnty_ar = models.CharField(_('warnty_ar'),max_length=250,blank=True)
    price_after_discount = property(lambda self: self.price - (self.price * self.discound / 100))
    class Meta:
        verbose_name_plural = _('Product')
    def __str__(self):
        return self.title

class About_Company(models.Model):
    title = models.CharField(_('title'),max_length=50)
    title_ar = models.CharField(_('title_ar'),max_length=50,blank=True)
    description = models.CharField(_('description'),max_length=150)
    description_ar = models.CharField(_('description_ar'),max_length=150,blank=True)
    icon_name = models.CharField(_('icon_name'),max_length=50)
    class Meta:
        verbose_name_plural = _('About_Company')
    def __str__(self):
        return self.title

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(_('full_name'),max_length=255)
    address = models.CharField(_('address'),max_length=255, blank=True,null=True)
    image = models.ImageField(_('image'),upload_to='client_images/')
    phone_number = models.CharField(_('phone_number'),max_length=15, blank=True, null=True)
    join_on = models.DateTimeField(_('join_on'),auto_now_add=True)
    class Meta:
        verbose_name_plural = _('Clients')
    def __str__(self):
        return self.full_name

class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.PositiveIntegerField(_('total'),default=0)
    created_at = models.DateTimeField(_('created_at'),auto_now_add=True)
    class Meta:
        verbose_name_plural = _('Cart')
    def __str__(self):
        return "Cart : " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(_('rate'),)
    quantity= models.PositiveIntegerField(_('quantity'),)
    subtotal = models.PositiveIntegerField(_('subtotal'),)
    class Meta:
        verbose_name_plural = _('CartProduct')
    def __str__(self):
        return "Cart : " + str(self.cart.id) + " Cart Product : " + str(self.id)

OREDER_STATUS = (
    (_('Order Received'), _('Order Received')),
    (_('Order Processing'), _('Order Processing')),
    (_('Order On The Way'), _('Order On The Way')),
    (_('Order Delivered'), _('Order Delivered')),
    (_('Order Cancelled'), _('Order Cancelled')),
)

PAYMET_METHOD = (
    (_('Cash On Delivery'), _('Cash On Delivery')),
    (_('Master Card'), _('Master Card')),
    (_('Visa Card'), _('Visa Card')),
    (_('Paypal'), _('Paypal')),
    (_('Fawry'), _('Fawry')),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    client = models.CharField(_('client'),max_length=255)
    shipping_address = models.CharField(_('shipping_address'),max_length=255)
    phone = models.CharField(_('phone'),max_length=15)
    email = models.EmailField(_('email'),null=True, blank=True)
    subtotal=models.PositiveIntegerField(_('subtotal'),)
    discount=models.PositiveIntegerField(_('discount'),)
    total=models.PositiveIntegerField(_('total'),)
    created_at = models.DateTimeField(_('created_at'),auto_now_add=True)
    order_status = models.CharField(_('order_status'),max_length=50, choices=OREDER_STATUS, default=_('Order Received'))
    payment_method = models.CharField(_('payment_method'),max_length=50, choices=PAYMET_METHOD, default=_('Cash On Delivery'))
    payment_completed = models.BooleanField(_('payment_completed'),default=False, blank=True, null=True)
    class Meta:
        verbose_name_plural = _('Order')
    def __str__(self):
        return "Order : " + str(self.id)