# Generated by Django 5.0.1 on 2024-01-21 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_notification_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content',
        ),
    ]
