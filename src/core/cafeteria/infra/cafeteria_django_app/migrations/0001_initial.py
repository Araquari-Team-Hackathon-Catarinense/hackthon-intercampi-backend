# Generated by Django 5.1.3 on 2024-11-27 19:29

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("campus_django_app", "0003_alter_classname_free_afternoons"),
    ]

    operations = [
        migrations.CreateModel(
            name="DietaryRestrictions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Cafeteria",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("max_students", models.IntegerField(default=300)),
                ("initial_time", models.TimeField()),
                ("final_time", models.TimeField()),
                (
                    "campus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cafeterias",
                        to="campus_django_app.campus",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("garnish", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "main_course",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("dessert", models.CharField(blank=True, max_length=255, null=True)),
                ("juice", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "dietary_restrictions",
                    models.ManyToManyField(
                        blank=True, to="cafeteria_django_app.dietaryrestrictions"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TurnstileEntrance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entry_time", models.DateTimeField(blank=True, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                ("payment", models.BooleanField(default=False)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="campus_django_app.student",
                    ),
                ),
            ],
        ),
    ]
