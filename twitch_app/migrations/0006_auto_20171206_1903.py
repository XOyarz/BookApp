# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_app', '0005_auto_20171206_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchuser',
            name='followers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='twitchuser',
            name='game',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='twitchuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
