# Generated by Django 3.0.8 on 2020-07-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0003_auto_20200722_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeaddress',
            name='landmark',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officeaddress',
            name='line1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officeaddress',
            name='line2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officeaddress',
            name='line3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officeaddress',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
