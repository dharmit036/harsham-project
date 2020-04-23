# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-24 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdb', '0002_auto_20200124_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('carnumber', models.CharField(max_length=10)),
                ('carmodel', models.CharField(max_length=50)),
                ('lastservice', models.CharField(max_length=10)),
                ('serviceintime', models.CharField(max_length=10)),
                ('predictedtime', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
