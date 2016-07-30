# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20160730_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='desired_comms',
            field=models.ManyToManyField(blank=True, help_text='Committee(s) requested by this candidate', related_name='desired_comms', to='committees.Committee'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='potential_comms',
            field=models.ManyToManyField(blank=True, help_text='Committee(s) being considered by LITA Appointments', related_name='potential_comms', to='committees.Committee'),
        ),
    ]
