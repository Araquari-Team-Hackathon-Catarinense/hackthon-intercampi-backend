from django.db import models
from core.campus.infra.campus_django_app.models import Student
from core.__seedwork__.infra.django_app.models import BaseModel


class PaymentSaveModel(models.Model):
    id = models.CharField(unique=True, max_length=155, primary_key=True)
    status = models.CharField(max_length=155, null=True, blank=True)
    status_detail = models.TextField(null=True, blank=True)
    transaction_amount = models.FloatField(default=0.0, blank=True, null=True)
    payment_method = models.CharField(max_length=155, null=True, blank=True)
    date_created = models.DateField(max_length=155, null=True, blank=True)
    qr_code = models.TextField(null=True, blank=True)
    qr_code_base64 = models.TextField(null=True, blank=True)
    date_approved = models.BooleanField(default=False, blank=True, null=True)
    time_approved = models.CharField(max_length=155, null=True, blank=True)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="payments",
        null=True,
        blank=True,
    )


class Credit(BaseModel):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="credit_students"
    )
    credit_value = models.FloatField(null=True, blank=True, default=0.0)
    date = models.DateField(null=True, blank=True)
    payment = models.ManyToManyField(
        PaymentSaveModel, related_name="credit_payment", null=True, blank=True
    )
