# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
