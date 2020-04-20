import json

from django.db import migrations
from constructor import models

JSON_PATH = {'CPU': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/cpu_json.json',
             'Motherboard': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/motherboards_json.json',
             'Video Card': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/video_cards_json.json',
             'Ram': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/rams_json.json',
             'Cooler': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/coolers_json.json',
             'Power Supply': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/cases_power_json.json',
             'Case': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/cases_power_json.json',
             'HDD': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/hdd_json.json',
             'DVD': '/Users/user/Desktop/Constructor/constructor_pc/parser/json_data/dvd_json.json'
             }


def add_parts_to_db(apps, schema_editor):
    for model, path in JSON_PATH.items():
        with open(path, 'r') as f:
            dict_cpu = json.load(f)
            for cpu in dict_cpu:

                if cpu.get('Price') == 'нет в наличии':
                    continue

                models.Product.objects.create(
                    name=str(cpu.get('Name')),
                    characteristics=cpu['Characteristics'],
                    price=float(str(cpu.get('Price')).replace('руб.', '').replace(',', '.').strip()),
                    category_id=models.Category.objects.get(name=model).id
                )


class Migration(migrations.Migration):
    dependencies = [
        ('constructor', '0002_add_data_to_db'),
    ]

    operations = [
        migrations.RunPython(add_parts_to_db)
    ]