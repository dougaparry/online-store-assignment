# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_item_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_source',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
