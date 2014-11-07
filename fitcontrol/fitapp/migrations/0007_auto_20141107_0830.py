# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0006_auto_20141107_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='dni',
            field=models.CharField(default='00000000A', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 7, 30, 53, 355970, tzinfo=utc), verbose_name='Fecha de nacimiento'),
            preserve_default=True,
        ),
    ]
