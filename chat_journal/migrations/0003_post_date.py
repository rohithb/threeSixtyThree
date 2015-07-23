# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat_journal', '0002_auto_20150722_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 17, 7, 4, 137267, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
