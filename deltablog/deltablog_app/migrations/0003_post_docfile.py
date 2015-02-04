# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltablog_app', '0002_auto_20150203_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
