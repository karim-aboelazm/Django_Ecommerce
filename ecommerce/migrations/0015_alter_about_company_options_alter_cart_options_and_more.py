# Generated by Django 4.1 on 2022-08-31 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0014_alter_product_description_ar_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about_company", options={"verbose_name_plural": "About_Company"},
        ),
        migrations.AlterModelOptions(
            name="cart", options={"verbose_name_plural": "Cart"},
        ),
        migrations.AlterModelOptions(
            name="cartproduct", options={"verbose_name_plural": "CartProduct"},
        ),
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Category"},
        ),
        migrations.AlterModelOptions(
            name="clients", options={"verbose_name_plural": "Clients"},
        ),
        migrations.AlterModelOptions(
            name="offer", options={"verbose_name_plural": "Offer"},
        ),
        migrations.AlterModelOptions(
            name="order", options={"verbose_name_plural": "Order"},
        ),
        migrations.AlterModelOptions(
            name="product", options={"verbose_name_plural": "Product"},
        ),
        migrations.AlterModelOptions(
            name="shoppy", options={"verbose_name_plural": "Shoppy"},
        ),
        migrations.AlterModelOptions(
            name="slider", options={"verbose_name_plural": "Slider"},
        ),
        migrations.AlterModelOptions(
            name="subscriber", options={"verbose_name_plural": "Subscriber"},
        ),
        migrations.AddField(
            model_name="about_company",
            name="description_ar",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="description_ar"
            ),
        ),
        migrations.AddField(
            model_name="about_company",
            name="title_ar",
            field=models.CharField(blank=True, max_length=50, verbose_name="title_ar"),
        ),
        migrations.AddField(
            model_name="category",
            name="title_ar",
            field=models.CharField(blank=True, max_length=50, verbose_name="title_ar"),
        ),
        migrations.AddField(
            model_name="offer",
            name="description_ar",
            field=models.TextField(blank=True, verbose_name="description_ar"),
        ),
        migrations.AddField(
            model_name="offer",
            name="title_ar",
            field=models.CharField(blank=True, max_length=250, verbose_name="title_ar"),
        ),
        migrations.AddField(
            model_name="shoppy",
            name="address_ar",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="address_ar"
            ),
        ),
        migrations.AddField(
            model_name="shoppy",
            name="description_ar",
            field=models.TextField(blank=True, verbose_name="description_ar"),
        ),
        migrations.AddField(
            model_name="shoppy",
            name="title_ar",
            field=models.CharField(blank=True, max_length=50, verbose_name="title_ar"),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_ar",
            field=models.CharField(blank=True, max_length=250, verbose_name="title_ar"),
        ),
        migrations.AlterField(
            model_name="about_company",
            name="description",
            field=models.CharField(max_length=150, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="about_company",
            name="icon_name",
            field=models.CharField(max_length=50, verbose_name="icon_name"),
        ),
        migrations.AlterField(
            model_name="about_company",
            name="title",
            field=models.CharField(max_length=50, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="cart",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
        ),
        migrations.AlterField(
            model_name="cart",
            name="total",
            field=models.PositiveIntegerField(default=0, verbose_name="total"),
        ),
        migrations.AlterField(
            model_name="cartproduct",
            name="quantity",
            field=models.PositiveIntegerField(verbose_name="quantity"),
        ),
        migrations.AlterField(
            model_name="cartproduct",
            name="rate",
            field=models.PositiveIntegerField(verbose_name="rate"),
        ),
        migrations.AlterField(
            model_name="cartproduct",
            name="subtotal",
            field=models.PositiveIntegerField(verbose_name="subtotal"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=50, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="clients",
            name="address",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="address"
            ),
        ),
        migrations.AlterField(
            model_name="clients",
            name="full_name",
            field=models.CharField(max_length=255, verbose_name="full_name"),
        ),
        migrations.AlterField(
            model_name="clients",
            name="image",
            field=models.ImageField(upload_to="client_images/", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="clients",
            name="join_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="join_on"),
        ),
        migrations.AlterField(
            model_name="clients",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="phone_number"
            ),
        ),
        migrations.AlterField(
            model_name="offer",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="offer",
            name="image",
            field=models.ImageField(upload_to="offer/", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="offer",
            name="rate",
            field=models.IntegerField(default=0, verbose_name="rate"),
        ),
        migrations.AlterField(
            model_name="offer",
            name="title",
            field=models.CharField(max_length=250, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="order",
            name="client",
            field=models.CharField(max_length=255, verbose_name="client"),
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
        ),
        migrations.AlterField(
            model_name="order",
            name="discount",
            field=models.PositiveIntegerField(verbose_name="discount"),
        ),
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="email"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Order Received", "Order Received"),
                    ("Order Processing", "Order Processing"),
                    ("Order On The Way", "Order On The Way"),
                    ("Order Delivered", "Order Delivered"),
                    ("Order Cancelled", "Order Cancelled"),
                ],
                default="Order Received",
                max_length=50,
                verbose_name="order_status",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_completed",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="payment_completed"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Cash On Delivery", "Cash On Delivery"),
                    ("Master Card", "Master Card"),
                    ("Visa Card", "Visa Card"),
                    ("Paypal", "Paypal"),
                    ("Fawry", "Fawry"),
                ],
                default="Cash On Delivery",
                max_length=50,
                verbose_name="payment_method",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(max_length=15, verbose_name="phone"),
        ),
        migrations.AlterField(
            model_name="order",
            name="shipping_address",
            field=models.CharField(max_length=255, verbose_name="shipping_address"),
        ),
        migrations.AlterField(
            model_name="order",
            name="subtotal",
            field=models.PositiveIntegerField(verbose_name="subtotal"),
        ),
        migrations.AlterField(
            model_name="order",
            name="total",
            field=models.PositiveIntegerField(verbose_name="total"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description_ar",
            field=models.TextField(blank=True, verbose_name="description_ar"),
        ),
        migrations.AlterField(
            model_name="product",
            name="discound",
            field=models.IntegerField(default=0, verbose_name="discound"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="product/", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="product",
            name="policy_return",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="policy_return"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="policy_return_ar",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="policy_return_ar"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0, verbose_name="price"),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=50, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="product",
            name="title_ar",
            field=models.CharField(blank=True, max_length=50, verbose_name="title_ar"),
        ),
        migrations.AlterField(
            model_name="product",
            name="warnty",
            field=models.CharField(blank=True, max_length=250, verbose_name="warnty"),
        ),
        migrations.AlterField(
            model_name="product",
            name="warnty_ar",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="warnty_ar"
            ),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="address",
            field=models.CharField(max_length=200, verbose_name="address"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="fb_link",
            field=models.URLField(blank=True, null=True, verbose_name="fb_link"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="icon",
            field=models.ImageField(upload_to="shoppy/", verbose_name="icon"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="ins_link",
            field=models.URLField(blank=True, null=True, verbose_name="ins_link"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="li_link",
            field=models.URLField(blank=True, null=True, verbose_name="li_link"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="phone"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="title",
            field=models.CharField(max_length=50, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="shoppy",
            name="tw_link",
            field=models.URLField(blank=True, null=True, verbose_name="tw_link"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="image",
            field=models.ImageField(upload_to="slider/", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="title",
            field=models.CharField(max_length=250, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="subscriber",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email"),
        ),
    ]