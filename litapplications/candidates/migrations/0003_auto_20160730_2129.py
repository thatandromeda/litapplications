# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0001_initial'),
        ('candidates', '0002_candidate_review_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='desired_comms',
            field=models.ManyToManyField(help_text='Committee(s) requested by this candidate', related_name='desired_comms', to='committees.Committee'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='potential_comms',
            field=models.ManyToManyField(help_text='Committee(s) being considered by LITA Appointments', related_name='potential_comms', to='committees.Committee'),
        ),
    ]
