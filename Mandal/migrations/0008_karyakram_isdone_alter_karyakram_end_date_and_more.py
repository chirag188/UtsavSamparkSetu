# Generated by Django 4.0.1 on 2022-02-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0007_rename_is_active_karyakram_start_attandance'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyakram',
            name='IsDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='karyakram',
            name='End_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Followup End Date'),
        ),
        migrations.AlterField(
            model_name='karyakram',
            name='Start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Followup Start Date'),
        ),
    ]