# Generated by Django 3.0.8 on 2020-08-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userquestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='Comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]
