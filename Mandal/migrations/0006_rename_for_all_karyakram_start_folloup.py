# Generated by Django 4.0.1 on 2022-02-14 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0005_mandalprofile_nirikshak_mandalprofile_sanchalak'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karyakram',
            old_name='For_All',
            new_name='Start_Folloup',
        ),
    ]