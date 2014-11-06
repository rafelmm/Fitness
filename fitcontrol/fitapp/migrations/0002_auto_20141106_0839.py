# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('direccion', models.ForeignKey(to='fitapp.Direccion')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='user',
        ),
        migrations.DeleteModel(
            name='Entrenador',
        ),
        migrations.RemoveField(
            model_name='gestor',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='gestor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Gestor',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='user',
        ),
        migrations.DeleteModel(
            name='Socio',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='locality',
        ),
        migrations.AddField(
            model_name='direccion',
            name='escalera',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='localidad',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='piso',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='puerta',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='cp',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
