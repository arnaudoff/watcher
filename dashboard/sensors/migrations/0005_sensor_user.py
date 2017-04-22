# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 05:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensors', '0004_auto_20170307_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]