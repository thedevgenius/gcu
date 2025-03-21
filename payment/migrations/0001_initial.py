# Generated by Django 5.1.7 on 2025-03-18 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('breakdown', models.JSONField(default=dict)),
                ('type', models.CharField(blank=True, choices=[('CRS', 'Course Fee'), ('ADM', 'Admission Fee'), ('EXM', 'Exam Fee')], max_length=5, null=True)),
                ('academic_year', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='academics.academicyear')),
                ('course', models.ManyToManyField(blank=True, to='academics.course')),
            ],
        ),
    ]
