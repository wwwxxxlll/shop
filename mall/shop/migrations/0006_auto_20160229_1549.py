# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160229_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergoods',
            name='order_id',
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order_id',
            field=models.ManyToManyField(to='shop.Order'),
        ),
    ]
