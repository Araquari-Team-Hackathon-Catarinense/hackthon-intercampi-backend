from django.contrib import admin

from .models import Campus,Student, Employee, ClassName

admin.site.register(Campus)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(ClassName)
