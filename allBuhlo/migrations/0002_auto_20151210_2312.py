# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allBuhlo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inglitr',
            name='ingname',
            field=models.ForeignKey(default='50', to='allBuhlo.Ingridient'),
            preserve_default=False,
        ),
    ]
