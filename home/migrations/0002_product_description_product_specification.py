# Generated by Django 4.1.3 on 2022-11-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="product",
            name="specification",
            field=models.TextField(blank=True),
        ),
    ]
