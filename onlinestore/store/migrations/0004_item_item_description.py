# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20150516_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.CharField(default=b' ', max_length=400),
        ),
    ]
