# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('status', models.IntegerField(blank=True, help_text=b'Status returned by sendgrid upon trying to send this. Blank if no attempt has been made to send.', null=True)),
            ],
            options={
                'verbose_name': 'EmailMessage',
                'verbose_name_plural': 'EmailMessages',
            },
        ),
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(choices=[(b'NEW_VOLUNTEER_FORM', b'NEW_VOLUNTEER_FORM')], max_length=30)),
                ('subject', models.CharField(help_text=b'The subject line of your email. {first_name} and {last_name} are available.', max_length=50)),
                ('body', models.TextField(help_text=b'The body of your email. {first_name} and {last_name} are available.')),
                ('from_name', models.CharField(help_text=b'Name of the person that this email should appear to be from', max_length=50)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='emailtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailType'),
        ),
    ]
