# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0002_auto_20141106_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='cp',
            field=models.CharField(null=True, max_length=5, blank=True),
            preserve_default=True,
        ),
    ]
