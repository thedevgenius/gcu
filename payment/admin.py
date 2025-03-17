from django.contrib import admin

from .models import FeeCategory, Fee
# Register your models here.

admin.site.register(FeeCategory)
admin.site.register(Fee)