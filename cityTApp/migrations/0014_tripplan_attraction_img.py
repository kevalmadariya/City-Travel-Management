# Generated by Django 5.0.1 on 2024-03-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0013_rename_departure_data_tripplan_departure_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripplan',
            name='attraction_img',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='attraction/'),
        ),
    ]