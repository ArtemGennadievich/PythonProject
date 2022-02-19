import requests
from bs4 import BeautifulSoup
import csv

'''У меня вопрос про запись файла в csv. Как сделать так, чтобы если например смотреть в экселе не просто в 
горизонтальный ряд было написано, а конкрентно по столбцам. То есть например : Столбец "Тема" и вниз пошли темы, 
дальше столбец например "Новость" и все новости в этом столбце и т.д.
И по озону вопрос , там есть вызов, в принте отображается , хотел сделать список актуальных акций, но Озон не дал мне 
полный html код, а выдал то что в принте , почему так? Ладно бы если он вообще ничего не прислал, вопросов бы не было.'''


def get_html(url):
    return requests.get(url).text


def bs(html):
    return BeautifulSoup(html, 'lxml')


def write_csv(dic):
    with open('news_csv.csv', 'a') as a:
        writer = csv.writer(a, lineterminator='\r')
        writer.writerow((
            dic['Заголовок'],
            dic['Текст'],
            dic['Ссылка на статью'],
            dic['Дата статьи'],
            dic['Просмотров'],
        ))


def write_csv2(dic):
    with open('news_csv.csv', 'a') as a:
        writer = csv.writer(a, lineterminator='\r')
        writer.writerow((
            dic['Дата'],
            dic['Погода'],
            dic['Пробки'],
            dic['Курс'],
        ))


def main():
    url = 'https://63.ru/text/'
    url2 = 'https://www.ozon.ru/info/actions/'
    file = bs(get_html(url))
    file2 = bs(get_html(url2))
    print(file2)
    stock = file2
    news = file.find_all('article', class_="_3-SyJ")
    head = file.find_all('div', class_='_2SSKi')
    for el in head:
        try:
            today_date = el.find('div', class_='_1FzpP').text.strip()
        except ValueError:
            today_date = ''
        try:
            weather = el.find('span', class_='_1aqn2').find_next().text
        except ValueError:
            weather = ''
        try:
            traffic = el.find("span", class_="_1DaHr").find_next().text
        except ValueError:
            traffic = ''
        try:
            curr = el.find_all('div', class_='_2DO9N')
            usd = []
            for i in curr:
                usd.append(i.find('span').text)
        except ValueError:
            curr = ''

        dict_for_write2 = {
            'Дата': f'Сегодня: {today_date}',
            'Погода': f' Погода: {weather}',
            'Пробки': f' Пробки: {traffic}',
            'Курс': f'Курсы валют: {usd}'

        }
        write_csv2(dict_for_write2)

        for el in news:
            try:
                news_art = el.find('h2', class_='_2V471').text
            except ValueError:
                news_art = ''
            try:
                url_news = el.find('h2', class_='_2V471').find('a').get('href')
            except ValueError:
                url_news = ''
            try:
                h = el.find('div', class_='_2PjoK').text.strip()
            except ValueError:
                h = ''
            try:
                date = el.find('div', class_='_1jj4Y _2wuaP').text
            except ValueError:
                date = ''
            try:
                views = el.find('span', class_='_1_eoa').text
            except ValueError:
                views = ''

            dict_for_write = {
                "Заголовок": f'Тема:{h}',
                "Текст": news_art,
                "Ссылка на статью": f' Ссылка на статью: {url[:-6]}{url_news}',
                "Дата статьи": f'Дата статьи: {date}',
                "Просмотров": f'Просмотров: {views}'
            }
            write_csv(dict_for_write)



if __name__ == '__main__':
    main()
