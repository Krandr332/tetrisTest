# Generated by Django 4.0.4 on 2022-05-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tetris', '0003_profile_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='line',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
