# Generated by Django 4.0.1 on 2022-02-13 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FolloWUp', '0006_alter_followup_present'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followup',
            old_name='Present',
            new_name='Coming',
        ),
    ]
