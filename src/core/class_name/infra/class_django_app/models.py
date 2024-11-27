from django.db import models

# Create your models here.

class ClassName(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    free_afternoons = models.JSONField(null=True,blank=True)
    free_lunch = models.BooleanField(default=False)

