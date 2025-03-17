from django.contrib import admin

from .models import AcademicYear, Department, Course, Subject, Schedule
# Register your models here.

admin.site.register(AcademicYear)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Schedule)
