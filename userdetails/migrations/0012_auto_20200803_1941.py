# Generated by Django 3.0.8 on 2020-08-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0011_auto_20200803_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
