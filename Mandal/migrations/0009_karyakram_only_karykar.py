# Generated by Django 4.0.1 on 2022-02-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0008_karyakram_isdone_alter_karyakram_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyakram',
            name='Only_Karykar',
            field=models.BooleanField(default=False),
        ),
    ]
