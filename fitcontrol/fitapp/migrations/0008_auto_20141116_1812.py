# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitapp', '0007_auto_20141107_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='IBAN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('entidad', models.PositiveIntegerField(default=0)),
                ('oficina', models.PositiveIntegerField(default=0)),
                ('dc', models.PositiveIntegerField(default=0)),
                ('cuenta', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateTimeField(verbose_name='Fecha de nacimiento', default=datetime.datetime(2014, 11, 16, 17, 12, 30, 78469, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
