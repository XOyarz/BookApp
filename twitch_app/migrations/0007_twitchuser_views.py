# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_app', '0006_auto_20171206_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchuser',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
