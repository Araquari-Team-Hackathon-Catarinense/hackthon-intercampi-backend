# Generated by Django 5.1.3 on 2024-11-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_django_app', '0005_alter_paymentsavemodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='payment',
            field=models.ManyToManyField(null=True, related_name='credit_payment', to='credit_django_app.paymentsavemodel'),
        ),
    ]
