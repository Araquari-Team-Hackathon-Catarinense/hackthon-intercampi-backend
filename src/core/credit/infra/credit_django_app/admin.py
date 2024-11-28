from django.contrib import admin

# Register your models here.
from .models import Credit, PaymentSaveModel

admin.site.register(Credit)
admin.site.register(PaymentSaveModel)
