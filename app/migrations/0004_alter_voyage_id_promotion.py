# Generated by Django 5.0 on 2024-01-14 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_utilisateur_id_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='id_promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.promotion'),
        ),
    ]