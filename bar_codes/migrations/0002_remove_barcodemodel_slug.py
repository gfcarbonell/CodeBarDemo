# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-03-02 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar_codes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcodemodel',
            name='slug',
        ),
    ]
