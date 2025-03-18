from django.db import models
from core.choices import FEE_TYPE_CHOICES

# Create your models here.
class FeeCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fee(models.Model):
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, blank=True)
    course = models.ManyToManyField('academics.Course', blank=True)
    due_date = models.DateField()
    breakdown = models.JSONField(default=dict)
    type = models.CharField(max_length=5, choices=FEE_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.due_date} - {self.type}'
    
    def get_total(self):
        total = 0
        for key, value in self.breakdown.items():
            total += int(value)
        return total
    
    def get_type(self):
        return dict(FEE_TYPE_CHOICES)[self.type]