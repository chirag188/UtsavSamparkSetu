# Generated by Django 4.0.1 on 2022-02-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0003_remove_yuvakprofile_addressline1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuvakprofile',
            name='Area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='yuvakprofile',
            name='HouseNo',
            field=models.IntegerField(verbose_name='House/Flat No.'),
        ),
        migrations.AlterField(
            model_name='yuvakprofile',
            name='LandMark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='yuvakprofile',
            name='Soc_Name',
            field=models.CharField(max_length=50, verbose_name='Sociaty/Apartment Name'),
        ),
    ]