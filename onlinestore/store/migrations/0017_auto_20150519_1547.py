# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20150519_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image_source',
        ),
        migrations.RemoveField(
            model_name='category',
            name='thumbnail',
        ),
    ]
