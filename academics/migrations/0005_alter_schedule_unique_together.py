# Generated by Django 5.1.7 on 2025-03-16 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_schedule'),
        ('accounts', '0004_teacher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('day', 'period', 'course', 'semester'), ('day', 'period', 'teacher')},
        ),
    ]
