# Generated by Django 4.0.1 on 2022-02-11 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SamparkKarykar', '0004_remove_karyakarprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karyakarprofile',
            old_name='profile',
            new_name='karykar1profile',
        ),
    ]
