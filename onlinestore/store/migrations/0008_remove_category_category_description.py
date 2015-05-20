# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_category_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_description',
        ),
    ]
