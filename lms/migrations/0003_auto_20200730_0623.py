# Generated by Django 3.0.8 on 2020-07-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20200730_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(),
        ),
    ]