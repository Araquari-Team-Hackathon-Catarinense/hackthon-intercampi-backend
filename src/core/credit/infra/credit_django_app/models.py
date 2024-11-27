from django.db import models
from core.campus.infra.campus_django_app.models import Student

# Create your models here.
class Credit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="credit_students")
    credit_value = models.FloatField(null=True, blank=True, default=0.0)
    date = models.DateField(null=True, blank=True)