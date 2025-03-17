# Generated by Django 5.1.7 on 2025-03-15 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0002_alter_department_code'),
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
                ('type', models.CharField(blank=True, max_length=5, null=True)),
                ('academic_year', models.ManyToManyField(blank=True, to='academics.academicyear')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.course')),
            ],
        ),
    ]
