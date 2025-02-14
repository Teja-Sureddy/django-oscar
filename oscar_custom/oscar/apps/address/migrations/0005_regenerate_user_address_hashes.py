# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 16:08
from __future__ import unicode_literals

from django.db import migrations

from oscar_custom.oscar.core.loading import get_model


ORMUserAddress = get_model('address', 'UserAddress')


def regenerate_user_address_hashes(apps, schema_editor):
    MigrationUserAddress = apps.get_model('address', 'UserAddress')
    for user_address in MigrationUserAddress.objects.all():
        orm_user_address = ORMUserAddress.objects.get(id=user_address.id)
        user_address.hash = orm_user_address.generate_hash()
        user_address.save()


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20170226_1122'),
    ]

    operations = [
        migrations.RunPython(regenerate_user_address_hashes, migrations.RunPython.noop)
    ]
