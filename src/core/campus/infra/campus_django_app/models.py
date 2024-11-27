import uuid

from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.campus.domain.value_objects import ContractType, PersonType
from core.uploader.infra.uploader_django_app.models import Document
from core.user.infra.user_django_app.models import User


class Campus(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    

 
    class Meta:
        db_table: str = "company"
        verbose_name_plural: str = "companies"

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"


class Employee(BaseModel):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    siape = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table: str = "employee"
        verbose_name_plural: str = "employees"

    def __str__(self) -> str:
        return f"{self.user} ({self.campus})"

class Student(BaseModel):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    registration = models.CharField(max_length=255, unique=True)
    is_cavalo = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table: str = "student"
        verbose_name_plural: str = "students"

    def __str__(self) -> str:
        return f"{self.user} ({self.campus})"


