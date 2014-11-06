# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitapp', '0004_auto_20141106_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='usuario',
        ),
        migrations.AddField(
            model_name='direccion',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
