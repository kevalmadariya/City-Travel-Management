# Generated by Django 5.0.1 on 2024-03-02 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0014_tripplan_attraction_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripplan',
            name='attraction_img',
        ),
    ]
