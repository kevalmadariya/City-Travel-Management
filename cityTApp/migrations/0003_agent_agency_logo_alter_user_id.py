# Generated by Django 5.0.1 on 2024-02-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0002_user_alter_tripplan_id_ticket_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agency_logo',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='img_Agc_logo/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]