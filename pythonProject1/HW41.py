from parse import Parser


def main():
    for i in range(15):
        par = Parser(f'https://www.e-katalog.ru/list/206/{i}', 'HW41.csv')
        par.get_html()
        par.parsing()
        par.count()
    print(par.middle_count())


if __name__ == '__main__':
    main()