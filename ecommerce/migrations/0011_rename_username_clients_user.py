# Generated by Django 4.1 on 2022-08-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0010_clients"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clients", old_name="username", new_name="user",
        ),
    ]
