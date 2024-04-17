# Generated by Django 4.2.4 on 2023-12-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_product_meta_robots_product_og_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='meta_robots',
        ),
        migrations.RemoveField(
            model_name='product',
            name='og_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='og_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='og_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='og_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='twitter_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='twitter_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='twitter_title',
        ),
        migrations.RemoveField(
            model_name='sub_categories',
            name='twitter_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_tag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(max_length=100),
        ),
    ]