from core.credit.infra.credit_django_app.models import Credit
from core.campus.infra.campus_django_app.models import Student
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Student)
def create_student_credit(sender, instance, created, **kwargs):
    if created:
        Credit.objects.create(student=instance, credit_value=300.0)
