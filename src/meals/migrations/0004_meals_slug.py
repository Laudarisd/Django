# Generated by Django 2.1.4 on 2018-12-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meals_preperation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
