# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allBuhlo', '0004_auto_20151210_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alcohol',
            name='ingridients',
        ),
        migrations.AddField(
            model_name='inglitr',
            name='alcohol',
            field=models.ForeignKey(default='0', to='allBuhlo.Alcohol'),
            preserve_default=False,
        ),
    ]
