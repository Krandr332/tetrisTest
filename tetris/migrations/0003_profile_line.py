# Generated by Django 4.0.4 on 2022-05-26 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tetris', '0002_alter_profile_score_alter_profile_top_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='line',
            field=models.CharField(default=0, max_length=50),
        ),
    ]