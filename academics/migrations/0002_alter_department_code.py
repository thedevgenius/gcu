# Generated by Django 5.1.7 on 2025-03-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
