# Generated by Django 5.0.1 on 2024-02-21 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('agency_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('gst_no', models.IntegerField()),
                ('upi_id', models.CharField(max_length=30)),
                ('about_us', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TripPlan',
            fields=[
                ('id', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('trip_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('departure_data', models.DateField()),
                ('departure_time', models.TimeField()),
                ('departure_place', models.CharField(max_length=30)),
                ('return_date', models.DateField()),
                ('return_time', models.TimeField()),
                ('return_place', models.CharField(max_length=30)),
                ('agency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cityTApp.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cityTApp.tripplan')),
            ],
        ),
    ]
