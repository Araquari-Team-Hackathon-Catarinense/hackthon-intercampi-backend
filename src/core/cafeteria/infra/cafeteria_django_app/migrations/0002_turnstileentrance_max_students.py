# Generated by Django 5.1.3 on 2024-11-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria_django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnstileentrance',
            name='max_students',
            field=models.IntegerField(default=300),
        ),
    ]
