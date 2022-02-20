import requests
from bs4 import BeautifulSoup
import re


class Parser:
    html = ''
    res = []
    change = []
    number_for_mid = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        r = requests.get(self.url).text
        self.html = BeautifulSoup(r, 'lxml')

    def reg(self, r):
        reg = r'до'
        reg2 = r'р.'
        chang = re.sub('\s', "", r)
        chang3 = re.sub(reg2, '', chang)
        chang2 = re.split(reg, chang3)
        Parser.change.append(chang2)

    def count(self):
        for i in Parser.change:
            if len(i) >= 2:
                diff = (int(i[1]) - int(i[0])) / 2
                Parser.number_for_mid.append(int(i[0]) + round(diff))
            else:
                Parser.number_for_mid.append(int(i[0]))

    def middle_count(self):
        print(f'Объявлений по продаже фотоаппаратов, на данный момент на сайте E.catalog: {len(Parser.number_for_mid)}')
        return f'Средняя цена всех фотоаппаратов на сайте E.catalog составляет: ' \
               f'{round(sum(Parser.number_for_mid) / len(Parser.number_for_mid), 2)} рублей'

    def parsing(self):
        first = self.html.find_all('td', class_='model-hot-prices-td')
        for i in first:
            sale = i.find('a').text
            self.reg(sale)
