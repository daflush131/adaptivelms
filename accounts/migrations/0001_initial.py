# Generated by Django 5.0 on 2024-01-27 18:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('year_and_section', models.CharField(blank=True, max_length=50, null=True)),
                ('course', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('user_type', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
