# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_item_image_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
