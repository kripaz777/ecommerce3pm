# Generated by Django 4.1.3 on 2022-11-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_product_description_product_specification"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReview",
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
                ("slug", models.CharField(max_length=400)),
                ("username", models.CharField(max_length=400)),
                ("email", models.EmailField(max_length=100)),
                ("review", models.TextField(blank=True)),
                ("star", models.IntegerField(default=1)),
            ],
        ),
    ]