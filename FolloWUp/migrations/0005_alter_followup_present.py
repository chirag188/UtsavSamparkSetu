# Generated by Django 4.0.1 on 2022-02-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FolloWUp', '0004_rename_samparkkarykar_followup_karykarvrund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='Present',
            field=models.IntegerField(blank=True, choices=[(1, 'Not_Sure'), (2, 'Yes'), (3, 'No'), (4, 'Unknown')], null=True),
        ),
    ]