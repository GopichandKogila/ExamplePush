# Generated by Django 5.0.7 on 2024-08-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
