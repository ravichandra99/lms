# Generated by Django 3.0.8 on 2020-07-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='python'),
        ),
    ]
