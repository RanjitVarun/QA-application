# Generated by Django 3.0.8 on 2020-07-21 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainskill', models.CharField(max_length=50)),
                ('subskill', models.IntegerField()),
            ],
            options={
                'db_table': 'skillset',
            },
        ),
        migrations.CreateModel(
            name='skillsetRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='usereduskill.Skillset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skill', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'skillsetrel',
            },
        ),
        migrations.CreateModel(
            name='EducationRelUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_relation', to='usereduskill.Board')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_relation', to='usereduskill.Course')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degree_relation', to='usereduskill.Education')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_relation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'educationreluser',
            },
        ),
    ]