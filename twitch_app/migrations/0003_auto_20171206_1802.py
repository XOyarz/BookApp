# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_app', '0002_auto_20171206_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitchuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
