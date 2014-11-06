# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0003_auto_20141106_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.AddField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(null=True, to='fitapp.Usuario'),
            preserve_default=True,
        ),
    ]
