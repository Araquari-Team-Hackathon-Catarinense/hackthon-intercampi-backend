import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campus_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSaveModel',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=155, null=True)),
                ('status_detail', models.TextField(blank=True, null=True)),
                ('transaction_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=155, null=True)),
                ('date_created', models.CharField(blank=True, max_length=155, null=True)),
                ('qr_code', models.TextField(blank=True, null=True)),
                ('qr_code_base64', models.TextField(blank=True, null=True)),
                ('date_approved', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('credit_value', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_students', to='campus_django_app.student')),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='credit_django_app.paymentsavemodel')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
