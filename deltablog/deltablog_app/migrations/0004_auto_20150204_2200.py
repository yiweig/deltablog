# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltablog_app', '0003_post_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
