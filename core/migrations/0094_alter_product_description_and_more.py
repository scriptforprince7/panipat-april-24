# Generated by Django 4.2.4 on 2024-02-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0093_alter_product_old_price_alter_product_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, default="This is the product", max_length=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="specifications",
            field=models.TextField(
                blank=True, default="N/A", max_length=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="productvarient",
            name="description",
            field=models.TextField(
                blank=True, default="This is the product", max_length=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="productvarient",
            name="specifications",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]