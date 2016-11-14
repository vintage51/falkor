# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falkor', '0006_auto_20161102_0455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('can_open_ide', 'Can open IDE'),)},
        ),
        migrations.AlterField(
            model_name='editortype',
            name='urlPrefix',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='editortype',
            name='urlSuffix',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]