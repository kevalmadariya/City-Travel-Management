# Generated by Django 5.0.1 on 2024-04-03 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0027_rename_ticket_id_passenger_t_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='t_id',
            new_name='ticket_id',
        ),
    ]
