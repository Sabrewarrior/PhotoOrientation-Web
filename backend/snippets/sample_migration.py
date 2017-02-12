'''
1. python manage.py makemigrations --empty <yourapp> --name load_intial_data
2. Edit your migration file <yourapp>/migrations/<highest>_auto_<###>.py using this sample file.
3. python manage.py migrate <yourapp>
'''

from __future__ import unicode_literals

from django.db import migrations

import os
from django.core import serializers

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filenames = ['fixtures_db.json', 'fixtures_urllist.json']


def load_fixture(apps, schema_editor):
    for fixture_filename in fixture_filenames:
        fixture_file = os.path.join(fixture_dir, fixture_filename)

        fixture = open(fixture_file, 'rb')
        objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
        for obj in objects:
            obj.save()
        fixture.close()


def unload_fixture(apps, schema_editor):
    MyModel = apps.get_model("snippets", "ModelName")
    MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]

