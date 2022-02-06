# Generated by Django 4.0.1 on 2022-02-06 15:58

import Yuvak.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0005_yuvakprofile_dateofbirth_yuvakprofile_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatsangProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NityaPuja', models.BooleanField(default=False)),
                ('NityaPujaYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('TilakChandlo', models.BooleanField(default=False)),
                ('TilakChandloYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('Satsangi', models.BooleanField(default=False)),
                ('SatsangiYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('AthvadikSabha', models.BooleanField(default=False)),
                ('AthvadikSabhaYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('Ravisabha', models.BooleanField(default=False)),
                ('RavisabhaYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('GharSatsang', models.BooleanField(default=False)),
                ('GharSatsangYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('SSP', models.BooleanField(default=False)),
                ('SSPStage', models.IntegerField(choices=[(0, 'No'), (1, 'prarambh'), (2, 'pravesh'), (3, 'parichay'), (4, 'paravin'), (5, 'Pragn_1'), (6, 'Pragn_2'), (7, 'Pragn_3')], default=Yuvak.models.SSPStage['No'])),
                ('Ekadashi', models.BooleanField(default=False)),
                ('EkadashiYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('Niymit_Vanchan', models.BooleanField(default=False)),
                ('Niymit_VanchanYear', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)])),
                ('yuvakProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Yuvak.yuvakprofile')),
            ],
        ),
    ]
