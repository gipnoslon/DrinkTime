# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allBuhlo', '0002_auto_20151210_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcohol',
            name='ingridients',
            field=models.ForeignKey(to='allBuhlo.IngLitr', default=0),
            preserve_default=False,
        ),
    ]
