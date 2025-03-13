from django.contrib import admin

from .models import AcademicYear, Grade, Subject, Department
# Register your models here.

admin.site.register(AcademicYear)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Department)