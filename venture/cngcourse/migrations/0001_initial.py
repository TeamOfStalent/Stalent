# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('year', models.DecimalField(max_digits=4, decimal_places=0)),
                ('name', models.CharField(max_length=20)),
                ('ID1', models.CharField(max_length=10)),
                ('school', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
