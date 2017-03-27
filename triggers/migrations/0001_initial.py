# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sensors', '0004_auto_20170307_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=65536)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_triggered', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.Sensor')),
            ],
        ),
        migrations.AddField(
            model_name='capture',
            name='trigger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triggers.Trigger'),
        ),
    ]