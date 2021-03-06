# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods')),
            ],
        ),
        migrations.RemoveField(
            model_name='buser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='fuser',
            name='status',
        ),
        migrations.AddField(
            model_name='buser',
            name='is_active',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuser',
            name='is_active',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='buser',
            table='shop_buser',
        ),
        migrations.AlterModelTable(
            name='fuser',
            table='shop_fuser',
        ),
    ]
