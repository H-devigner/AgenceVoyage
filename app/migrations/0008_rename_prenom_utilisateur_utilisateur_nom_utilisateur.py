# Generated by Django 5.0 on 2024-01-22 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_utilisateur_prenom_utilisateur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='prenom_utilisateur',
            new_name='nom_utilisateur',
        ),
    ]
