# Generated by Django 3.0.7 on 2020-07-12 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_board_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degree_course', to='user.Education'),
        ),
    ]
