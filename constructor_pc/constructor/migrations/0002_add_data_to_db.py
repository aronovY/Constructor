import json

from django.db import migrations
from constructor import models

JSON_PATH = ['CPU',
             'Motherboard',
             'Video Card',
             'Ram',
             'Cooler',
             'Power Supply',
             'Case',
             'HDD',
             'DVD',
             ]


def add_category_to_db(apps,schema_editor):
    for key in JSON_PATH:
        models.Category.objects.create(
            name=key
        )


class Migration(migrations.Migration):
    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_category_to_db)
    ]