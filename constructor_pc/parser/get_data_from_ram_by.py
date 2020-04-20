import http
import json
import requests
from bs4 import BeautifulSoup

REPL = {'\t': '', '\n': '', '\r': '', '\"': ''}

#  All links for parsing RAM.by

DICT_OF_URLS = {
        'CPU': 'https://ram.by/parts/cpu.html?page=',
        'MOTHERBOARDS': 'https://ram.by/parts/motherboards.html?page=',
        'VIDEO_CARDS': 'https://ram.by/parts/videocard.html?page=',
        'RAMS': 'https://ram.by/parts/ram.html?page=',
        'COOLERS': 'https://ram.by/parts/coolers.html?page=',
        'WATER_COOL': 'https://ram.by/sistemy-vodyanogo-ohlazhdeniya',
        'HDD': 'https://ram.by/parts/hdd.html?page=',
        'DVD': 'https://ram.by/parts/dvd.html?page=',
        'CASES_POWER': 'https://ram.by/parts/cases-and-power-supply.html?page='
}

LAST_PAGES = {
    'CPU': 30,
    'MOTHERBOARDS': 30,
    'VIDEO_CARDS': 40,
    'RAMS': 60,
    'COOLERS': 40,
    'WATER_COOL': 2,
    'HDD': 55,
    'DVD': 8,
    'CASES_POWER': 100
}


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


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


def get_content_data(html, raw_data):
    """
    We get the information we need from the html pages and save it in the dictionary.
    :param html: HTML page as text
    :param raw_data: The dictionary in which the received data is saved
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="item")

    for item in items:

        name = item.find('div', class_='title')
        description = item.find('div', class_='desciption')

        if description.find('a') is None:
            break

        link_characteristic = description.find('a')['href']  # or item.find('a').get('href')
        html_cpu = get_html(str(link_characteristic))

        if html_cpu.status_code == http.HTTPStatus.OK:
            name_of_characteristics = []
            description_of_characteristics = []
            soup_cpu = BeautifulSoup(html_cpu.text, 'html.parser')
            data_parts = soup_cpu.find_all('table')  # or soup_cpu.find_all('table', {'border': '0'})

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

                information_of_part_in_dict = dict(zip(name_of_characteristics, description_of_characteristics))

                raw_data.append({
                    'Name': replace_all(name.find('a').text, REPL),
                    'Characteristics': information_of_part_in_dict,
                    'Price': money
                })
        else:
            print('Error')


def parse(name, url):
    """
    In this method we parse all links and get raw data that we convert to .json files for further work with them.
    """
    list_data = []
    if name == 'WATER_COOL':
        html = get_html(str(url))
        if html.status_code == http.HTTPStatus.OK:
            get_content_data(html.text, list_data)
            path_json = f'json_data/{name.lower()}_json.json'
            save_data_to_json_file(list_data, path_json)
        else:
            print('Error')
    else:
        for page in range(LAST_PAGES[name]):
            html = get_html(str(url) + str(page))
            if html.status_code == http.HTTPStatus.OK:
                get_content_data(html.text, list_data)
                path_json = f'json_data/{name.lower()}_json.json'
                save_data_to_json_file(list_data, path_json)
            else:
                print('Error')


def save_data_to_json_file(dict_of_data, path):
    """
    Convert data to .json
    :param dict_of_data: Data of parts
    :param path: Path to save .json
    :return: Save .json file
    """
    with open(path, 'w') as json_file:
        json_str = json.dumps(dict_of_data, indent=2, ensure_ascii=False, separators=(',', ': '))
        json_file.write(json_str)


def get_data_from_ram_by():
    for key, item in DICT_OF_URLS.items():
        parse(key, item)



get_data_from_ram_by()