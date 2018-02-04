# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youminer', '0006_customuser_nbquizz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.CharField(default='', max_length=255, primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=255)),
                ('created_date', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youminer.Video')),
            ],
        ),
    ]