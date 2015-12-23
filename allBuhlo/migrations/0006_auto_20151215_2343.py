# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allBuhlo', '0005_auto_20151212_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inglitr',
            name='alcohol',
        ),
        migrations.AddField(
            model_name='alcohol',
            name='ingredients',
            field=models.ManyToManyField(to='allBuhlo.IngLitr'),
        ),
    ]
