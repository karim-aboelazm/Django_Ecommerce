# Generated by Django 4.1 on 2022-08-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ecommerce", "0002_delete_clients"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shoppy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("icon", models.ImageField(upload_to="shoppy/")),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=200)),
                ("fb_link", models.URLField(blank=True, null=True)),
                ("tw_link", models.URLField(blank=True, null=True)),
                ("ins_link", models.URLField(blank=True, null=True)),
                ("li_link", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
