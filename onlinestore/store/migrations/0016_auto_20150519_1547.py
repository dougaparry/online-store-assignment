# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20150519_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default=b'', null=True, upload_to=b'thumbs/'),
        ),
    ]
