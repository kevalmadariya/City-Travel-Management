# Generated by Django 5.0.1 on 2024-03-02 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0016_attraction_att_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='trip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cityTApp.tripplan', to_field='trip_name'),
        ),
    ]