# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0006_travels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='traveldate_from',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='travels',
            name='traveldate_to',
            field=models.CharField(max_length=50),
        ),
    ]
