# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='image',
            field=models.TextField(default=b''),
        ),
    ]