# Generated by Django 4.0.1 on 2022-02-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0005_mandalprofile_nirikshak_mandalprofile_sanchalak'),
        ('Yuvak', '0014_csvtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuvakprofile',
            name='mandal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mandal.mandalprofile'),
        ),
    ]