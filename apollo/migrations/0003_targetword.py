# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-15 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo', '0002_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30)),
            ],
        ),
    ]
