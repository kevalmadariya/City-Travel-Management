# Generated by Django 5.0.1 on 2024-03-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0011_tripplan_extra_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripplan',
            name='trip_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
