# Generated by Django 4.2.4 on 2023-09-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_sub_category_carpet_rolls_brands"),
    ]

    operations = [
        migrations.AddField(
            model_name="sub_category",
            name="awning_canopy_brands",
            field=models.BooleanField(default=False),
        ),
    ]