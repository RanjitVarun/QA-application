# Generated by Django 3.0.8 on 2020-07-29 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usereducationskill', '0003_auto_20200728_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsetrel',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='usereducationskill.Skillset'),
        ),
    ]
