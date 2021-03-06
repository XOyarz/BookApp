# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_app', '0008_auto_20171206_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchuser',
            name='profile_link',
            field=models.URLField(default='not'),
        ),
        migrations.AlterField(
            model_name='twitchuser',
            name='bio',
            field=models.TextField(default='No bio available'),
        ),
        migrations.AlterField(
            model_name='twitchuser',
            name='game',
            field=models.CharField(default='No game available', max_length=50),
        ),
    ]
