# Generated by Django 5.0.1 on 2024-03-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0020_alter_attraction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripplan',
            name='thumbnail',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='thumnail/'),
        ),
    ]