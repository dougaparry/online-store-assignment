# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20150519_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, default=b'', null=True, upload_to=b'thumbs/'),
        ),
    ]
