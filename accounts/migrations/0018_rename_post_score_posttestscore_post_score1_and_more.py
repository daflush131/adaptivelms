# Generated by Django 4.2.5 on 2024-02-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_pretestscore_pre_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttestscore',
            old_name='post_score',
            new_name='post_score1',
        ),
        migrations.AddField(
            model_name='posttestscore',
            name='post_score2',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posttestscore',
            name='post_score3',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posttestscore',
            name='post_score4',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
