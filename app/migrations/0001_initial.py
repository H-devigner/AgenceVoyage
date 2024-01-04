
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_categorie', models.AutoField(primary_key=True, serialize=False)),
                ('nom_categorie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id_hotel', models.AutoField(primary_key=True, serialize=False)),
                ('prix_nuit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('type_chambre', models.CharField(max_length=50)),
                ('type_hotel', models.IntegerField()),
                ('n_chambreDispo', models.IntegerField()),
                ('nom_hotel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id_images', models.AutoField(primary_key=True, serialize=False)),
                ('path_image', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('date_notif', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=15)),
                ('heure_d_notif', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id_pays', models.AutoField(primary_key=True, serialize=False)),
                ('nom_pays', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id_promotion', models.AutoField(primary_key=True, serialize=False)),
                ('date_d_promo', models.DateField()),
                ('date_f_promo', models.DateField()),
                ('heure_d_promos', models.TimeField()),
                ('heure_f_promos', models.TimeField()),
                ('pourcentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id_vol', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_d_vol', models.DateField()),
                ('date_f_vol', models.DateField()),
                ('prix_vol', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='ImageHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('id_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id_utilisateur_1', models.AutoField(primary_key=True, serialize=False)),
                ('mot_d_passe', models.CharField(max_length=10)),
                ('est_admin', models.BooleanField()),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('num_telephone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('path_img_profile', models.CharField(max_length=100)),
                ('id_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Recevoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.notification')),
                ('id_utilisateur_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id_ville', models.AutoField(primary_key=True, serialize=False)),
                ('nom_ville', models.CharField(max_length=50)),
                ('id_pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pays')),
            ],
        ),
        migrations.CreateModel(
            name='ImageVille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
                ('id_ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ville')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='id_ville',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ville'),
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id_voyage', models.AutoField(primary_key=True, serialize=False)),
                ('titre_voyage', models.CharField(max_length=50)),
                ('prix_voyage', models.DecimalField(decimal_places=2, max_digits=15)),
                ('duree_voyage', models.IntegerField()),
                ('transport', models.BooleanField()),
                ('id_categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
                ('id_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('id_promotion', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.promotion')),
            ],
        ),
        migrations.CreateModel(
            name='ReserverVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_utilisateur_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='inclure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vol')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id_comment', models.AutoField(primary_key=True, serialize=False)),
                ('text_comment', models.CharField(max_length=150)),
                ('date_redaction', models.DateField()),
                ('heure_redaction', models.TimeField()),
                ('evaluation', models.IntegerField()),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Avoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ville')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Aimer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_utilisateur_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voyage')),
            ],
        ),
    ]
