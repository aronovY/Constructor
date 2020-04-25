#! /usr/bin/env python
# -*- coding: utf-8 -*-

import http
import requests
from bs4 import BeautifulSoup

from constructor.models import Product, Category

REPL = {'\t': '', '\n': '', '\r': '', '\"': ''}

#  All links for parsing RAM.by

DICT_OF_URLS = {
        'CPU': 'https://ram.by/parts/cpu.html?page=',
        'MOTHERBOARDS': 'https://ram.by/parts/motherboards.html?page=',
        'VIDEO CARDS': 'https://ram.by/parts/videocard.html?page=',
        'RAMS': 'https://ram.by/parts/ram.html?page=',
        'COOLERS': 'https://ram.by/parts/coolers.html?page=',
        'HDD': 'https://ram.by/parts/hdd.html?page=',
        'DVD': 'https://ram.by/parts/dvd.html?page=',
        'CASES POWER': 'https://ram.by/parts/cases-and-power-supply.html?page='
}

LAST_PAGES = {
    'CPU': 30,
    'MOTHERBOARDS': 30,
    'VIDEO CARDS': 40,
    'RAMS': 60,
    'COOLERS': 40,
    'HDD': 55,
    'DVD': 8,
    'CASES POWER': 100
}


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


def get_photo(img, name, category):
    p = requests.get(img)
    out = open(f"constructor/templates/static/img/{category}/{str(name.replace(' ', '').replace('/', ''))}.jpg", 'wb')
    out.write(p.content)
    out.close()
    return f"static/img/{category}/{str(name.replace(' ', '').replace('/', ''))}.jpg"


def replace_all(text, dic):
    for i, to in dic.items():
        text = text.replace(i, to)
    return text.strip()


def get_html(url, params=None):
    """
    We get a Response object called response. Using this object you can get all the necessary information.
    :param url: link
    :param params:
    :return: Response object
    """
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content_data(html, category):
    """
    We get the information we need from the html pages and save it in the dictionary.
    :param html: HTML page as text
    :param category: Category of Product
    """
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_="item")

    for item in items:

        name = item.find('div', class_='title')
        description = item.find('div', class_='desciption')
        small_photo_url = item.find('div', class_='image').find('img')['data-src']

        if description.find('a') is None:
            break

        link_characteristic = description.find('a')['href']  # or item.find('a').get('href')
        html_cpu = get_html(str(link_characteristic))

        if html_cpu.status_code == http.HTTPStatus.OK:
            name_of_characteristics = []
            description_of_characteristics = []
            soup_part = BeautifulSoup(html_cpu.text, 'lxml')
            data_parts = soup_part.find_all('table')  # or soup_cpu.find_all('table', {'border': '0'})
            big_photo_url = soup_part.find('div', class_='photo').find('span', class_='boxer').find('img')['src']
            for part in data_parts:
                name_character = part.find_all('td', class_='param-name')

                if not name_character:
                    continue

                description_character = part.find_all('td', class_=None)
                for character in name_character:
                    name_of_characteristics.append(
                        replace_all(character.text, REPL)
                    )
                for description_chr in description_character:
                    description_of_characteristics.append(
                            replace_all(description_chr.text, REPL)
                    )

                if not item.find('div', class_='price')('span'):
                    money = replace_all(item.find('div', class_='price').text, REPL)
                else:
                    money = replace_all(item.find('div', class_='price')('span')[0].text, REPL)

                if money == 'нет в наличии':
                    continue

                information_of_part_in_dict = dict(zip(name_of_characteristics, description_of_characteristics))

                if Product.objects.filter(name=replace_all(name.find('a').text, REPL)):
                    continue
                else:
                    sf = get_photo(small_photo_url, replace_all(name.find('a').text, REPL), category)
                    bf = get_photo(big_photo_url, replace_all(name.find('a').text, REPL) + '2', category)
                    prod = Product.objects.create(
                        name=replace_all(name.find('a').text, REPL),
                        category_id=Category.objects.get(name=category).id,
                        characteristics=information_of_part_in_dict,
                        small_photo_link=sf,
                        big_photo_link=bf,
                        price=float(money.replace('руб.', '').replace(',', '.').strip())
                    )
                    prod.save()
        else:
            print('Error')


def parse(name, url):
    """
    In this method we parse all links and get raw data that we convert to .json files for further work with them.
    """
    for page in range(LAST_PAGES[name]):
        html = get_html(str(url) + str(page))
        if html.status_code == http.HTTPStatus.OK:
            get_content_data(html.text, name)
        else:
            print('Error')


def get_data_from_ram_by():
    for key, item in DICT_OF_URLS.items():
        parse(key, item)


get_data_from_ram_by()