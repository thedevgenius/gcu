# Generated by Django 5.1.7 on 2025-03-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('TEA', 'Teacher'), ('ADM', 'Admission'), ('RCP', 'Receptionist'), ('ACT', 'Accountant')], max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.CharField(choices=[('', '--- Select Blood Group ---'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
    ]
