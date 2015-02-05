# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deltablog_app', '0004_auto_20150204_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='docfile',
            new_name='image',
        ),
    ]
