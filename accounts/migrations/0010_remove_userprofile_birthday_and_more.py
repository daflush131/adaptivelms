# Generated by Django 5.0 on 2024-01-28 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_pretestscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_teacher',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='middle_name',
        ),
    ]
