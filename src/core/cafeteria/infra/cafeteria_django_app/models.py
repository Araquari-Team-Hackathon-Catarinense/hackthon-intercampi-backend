from django.db import models
from core.campus.infra.campus_django_app.models import Student

class DietaryRestrictions(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

# Create your models here.
class Menu(models.Model):
    garnish = models.CharField(max_length=255, null=True, blank=True)
    main_course = models.CharField(max_length=255, null=True, blank=True)
    dessert = models.CharField(max_length=255, null=True, blank=True)
    juice = models.CharField(max_length=255, null=True, blank=True)
    dietary_restrictions = models.ManyToManyField(DietaryRestrictions, blank=True)

    def __str__(self):
        return f"{self.garnish} - {self.main_course} - {self.dessert} - {self.juice}"
    

class TurnstileEntrance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name="students")
    entry_time = models.DateTimeField(null=True,blank=True)
    date = models.DateField(null=True, blank=True)
    payment = models.BooleanField(default=False)
    max_students = models.IntegerField(default=300)