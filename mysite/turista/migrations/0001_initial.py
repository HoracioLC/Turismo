# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('region', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('nombree', models.CharField(max_length=50, serialize=False, primary_key=True, db_column='nombreE')),
                ('calle', models.CharField(max_length=50)),
                ('num', models.CharField(max_length=10)),
                ('otro', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('web', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'info',
                'managed': False,
            },
        ),
    ]
