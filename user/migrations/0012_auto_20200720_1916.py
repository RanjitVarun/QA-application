# Generated by Django 3.0.8 on 2020-07-20 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200719_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='last_login',
        ),
    ]