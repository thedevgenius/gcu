from django.db import models

# Create your models here.
class FeeCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fee(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    course = models.ForeignKey('academics.Course', on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    breakdown = models.JSONField(default=dict)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.due_date} - {self.course}'