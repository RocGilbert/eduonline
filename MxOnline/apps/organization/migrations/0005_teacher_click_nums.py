# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-18 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180217_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
