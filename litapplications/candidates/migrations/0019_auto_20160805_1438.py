# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0018_auto_20160805_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'permissions': (('can_appoint', 'Can appoint committee members'),), 'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointments'},
        ),
    ]
