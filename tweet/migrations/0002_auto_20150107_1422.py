# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(verbose_name=b'default date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='retweet',
            name='date_retweeted',
            field=models.DateTimeField(verbose_name=b'default date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='date_created',
            field=models.DateTimeField(verbose_name=b'default date'),
            preserve_default=True,
        ),
    ]
