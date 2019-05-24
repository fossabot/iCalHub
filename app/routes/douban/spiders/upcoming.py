import urllib.request

import moment
from lxml import html
from cssselect import GenericTranslator


def read_document() -> str:
    with urllib.request.urlopen('https://movie.douban.com/coming') as page:
        return page.read().decode('utf-8')


def get_table_rows():
    document: str = read_document()
    tree = html.fromstring(document)

    expression = GenericTranslator().css_to_xpath('.coming_list tbody tr')

    elements = tree.xpath(expression)

    return elements


def get_movie_date(element) -> str:
    expression = GenericTranslator().css_to_xpath('td:nth-of-type(1)')

    date: str = element.xpath(expression)[0].text.strip()

    return date


def get_movie_name(element) -> str:
    expression = GenericTranslator().css_to_xpath('td:nth-of-type(2) a')

    name: str = element.xpath(expression)[0].text.strip()

    return name


def get_movie_item():
    elements = get_table_rows()

    for element in elements:
        try:
            date: str = get_movie_date(element)
            date = moment.date(date).strftime('%Y%m%d')
            stamp: str = '{}T000000Z'.format(date)

            name: str = get_movie_name(element)

            yield {
                'date': date,
                'name': name,
                'stamp': stamp,
            }
        except AttributeError:
            continue
