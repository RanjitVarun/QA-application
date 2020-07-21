# Generated by Django 3.0.8 on 2020-07-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200717_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
