# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0032_initialize_form_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='form_date',
        ),
    ]
