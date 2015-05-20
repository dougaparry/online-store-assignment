# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20150519_1428'),
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
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
