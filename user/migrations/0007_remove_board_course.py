# Generated by Django 3.0.7 on 2020-07-10 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200710_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='course',
        ),
    ]
