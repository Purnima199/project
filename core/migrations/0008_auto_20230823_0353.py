# Generated by Django 2.2.14 on 2023-08-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20230822_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(),
        ),
    ]
