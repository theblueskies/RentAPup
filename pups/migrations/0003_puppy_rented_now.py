# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pups', '0002_auto_20171015_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppy',
            name='rented_now',
            field=models.BooleanField(default=False),
        ),
    ]
