# Generated by Django 5.0.1 on 2024-03-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0022_tempticket_alter_passenger_ticket_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempticket',
            old_name='id',
            new_name='temp_id',
        ),
    ]