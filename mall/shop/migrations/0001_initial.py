# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=20)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commenttime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consignees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=100)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('tel', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Fuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('sex', models.CharField(blank=True, max_length=2, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tel', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('sale_price', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('descriptiont', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('status', models.IntegerField(blank=True, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('paddr', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_serial', models.IntegerField(unique=True)),
                ('descriptiont', models.TextField(blank=True, null=True)),
                ('order_genrate_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Consignees')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Buser')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.PayMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Fuser'),
        ),
        migrations.AddField(
            model_name='fuser',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Userstatus'),
        ),
        migrations.AddField(
            model_name='consignees',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Fuser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Fuser'),
        ),
        migrations.AddField(
            model_name='buser',
            name='permisson',
            field=models.ManyToManyField(to='shop.Permission'),
        ),
        migrations.AddField(
            model_name='buser',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Userstatus'),
        ),
    ]
