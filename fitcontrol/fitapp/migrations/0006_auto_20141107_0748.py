# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0005_auto_20141106_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='pais',
            field=models.CharField(default='ES', max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateTimeField(verbose_name='Fecha de nacimiento', default=datetime.datetime(2014, 11, 7, 6, 48, 27, 60331, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
