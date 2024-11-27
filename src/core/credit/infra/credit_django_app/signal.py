from core.credit.infra.credit_django_app.models import PaymentSaveModel, Credit

from django.dispatch import receiver
from django.db.models.signals import post_save



@receiver(post_save, sender=PaymentSaveModel)
def payment_is_approved(sender, instance, **kwargs):
    if instance.status == "approved":
        print("Payment is approved")
        try:
            credit = Credit.objects.get(payment=instance)
            instance.transaction_amount = credit.credit_value
            instance.save()
            credit.save()
        except Credit.DoesNotExist:
            print(f"No Credit associated with Payment ID {instance.id}")