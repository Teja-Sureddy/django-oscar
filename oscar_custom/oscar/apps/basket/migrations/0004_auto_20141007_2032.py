# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar_custom.oscar.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_basket_vouchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='price_currency',
            field=models.CharField(default=oscar_custom.oscar.core.utils.get_default_currency, max_length=12, verbose_name='Currency'),
        ),
    ]
