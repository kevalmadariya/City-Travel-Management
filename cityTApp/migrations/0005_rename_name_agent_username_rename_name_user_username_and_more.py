# Generated by Django 5.0.1 on 2024-02-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityTApp', '0004_alter_agent_agency_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
