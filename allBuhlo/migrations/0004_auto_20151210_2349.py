# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allBuhlo', '0003_alcohol_ingridients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alcohol',
            name='ingridients',
        ),
        migrations.AddField(
            model_name='alcohol',
            name='ingridients',
            field=models.ManyToManyField(to='allBuhlo.IngLitr'),
        ),
    ]
