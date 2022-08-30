from django.db import models
from django.contrib.auth.models import User

class Shoppy(models.Model):
    icon        = models.ImageField(upload_to="shoppy/")
    title       = models.CharField(max_length=50)
    description = models.TextField()
    phone       = models.CharField(max_length=20)
    address     = models.CharField(max_length=200)
    fb_link     = models.URLField(blank=True, null=True)
    tw_link     = models.URLField(blank=True, null=True)
    ins_link    = models.URLField(blank=True, null=True)
    li_link     = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title
        
class Offer(models.Model):
    title = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="offer/")
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50,blank=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True)
    image = models.ImageField(upload_to="product/")
    price = models.IntegerField(default=0)
    discound = models.IntegerField(default=0)
    policy_return = models.CharField(max_length=250,blank=True)
    policy_return_ar = models.CharField(max_length=250,blank=True)
    warnty = models.CharField(max_length=250,blank=True)
    warnty_ar = models.CharField(max_length=250,blank=True)
    price_after_discount = property(lambda self: self.price - (self.price * self.discound / 100))
    def __str__(self):
        return self.title

class About_Company(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    icon_name = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Clients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to='client_images/')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    join_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name

class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Cart : " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity= models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    def __str__(self):
        return "Cart : " + str(self.cart.id) + " Cart Product : " + str(self.id)

OREDER_STATUS = (
    ('Order Received', 'Order Received'),
    ('Order Processing', 'Order Processing'),
    ('Order On The Way', 'Order On The Way'),
    ('Order Delivered', 'Order Delivered'),
    ('Order Cancelled', 'Order Cancelled'),
)
PAYMET_METHOD = (
    ('Cash On Delivery', 'Cash On Delivery'),
    ('Master Card', 'Master Card'),
    ('Visa Card', 'Visa Card'),
    ('Paypal', 'Paypal'),
    ('Fawry', 'Fawry'),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    client = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, choices=OREDER_STATUS, default='Order Received')
    payment_method = models.CharField(max_length=50, choices=PAYMET_METHOD, default='Cash On Delivery')
    payment_completed = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return "Order : " + str(self.id)