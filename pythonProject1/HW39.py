import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London'],
        ['sw2', 'Cisco', '3850', 'Liverpool'],
        ['sw3', 'Cisco', '3650', 'Liverpool'],
        ['sw4', 'Cisco', '3650', 'London']]

'''Вообщем по домашке не понял как именно надо было сделать, сделал и так и так'''
'''И ещё есть вопрос по Гит хабу, скорее всего во вторник после занятия задам вопрос'''


def wrt_csv(d):
    with open('file_hw.csv', 'w') as w:
        dat = csv.writer(w, d, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\r')
        for i in d:
            dat.writerow(i)


def wrt_csv_2(d):
    with open('file_hw2.csv', 'w') as w:
        dat = csv.writer(w, d, delimiter=';', lineterminator='\r')
        for i in d:
            dat.writerow(i)


wrt_csv(data)
wrt_csv_2(data)
