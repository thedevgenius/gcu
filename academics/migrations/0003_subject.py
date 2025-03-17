# Generated by Django 5.1.7 on 2025-03-16 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_alter_department_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=50)),
                ('credit', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.course')),
            ],
        ),
    ]
