# Generated by Django 4.2.5 on 2024-02-01 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_pretestscore_pre_score1_pretestscore_pre_score2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pretestscore',
            name='pre_score',
        ),
    ]