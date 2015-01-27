# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=6, serialize=False, primary_key=True)),
                ('httpurl', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
