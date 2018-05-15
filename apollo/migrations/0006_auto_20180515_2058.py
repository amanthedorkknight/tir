# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-15 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo', '0005_player_is_logged_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetword',
            name='completed_from',
            field=models.CharField(default='car', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='targetword',
            name='completed_in',
            field=models.IntegerField(default=0),
        ),
    ]