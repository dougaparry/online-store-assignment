# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_category_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_source',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=b'thumbs/'),
        ),
    ]
