# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-03 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0002_coinresult_is_open_sourced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinresult',
            name='coin_id',
        ),
        migrations.AddField(
            model_name='coinresult',
            name='id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]