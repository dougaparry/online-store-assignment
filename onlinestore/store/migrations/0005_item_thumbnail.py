# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_item_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=b'thumbs/'),
        ),
    ]
