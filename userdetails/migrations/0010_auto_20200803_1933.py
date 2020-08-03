# Generated by Django 3.0.8 on 2020-08-03 19:33

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0009_auto_20200723_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile',
            field=phone_field.models.PhoneField(blank=True, max_length=12, unique=True),
        ),
    ]
