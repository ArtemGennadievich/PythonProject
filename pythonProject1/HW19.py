import re
password = '1qaz@_a'
reg = r'^([a-z-1-9-@-_]{6,18})$'
print(re.findall(reg, password))
data = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимум ежемесячных осадков.'
reg2 = r'([0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9])'
print(re.findall(reg2, data))

phone_numbers = '+7 499 455-45-78,' \
                '+74994564578,' \
                '7 (499) 456 46 78,' \
                '7 (499) 456-45-78,'
reg3 = r'([+7|7][\s\d{3}|(\d)-]*)'
print(re.findall(reg3, phone_numbers))
input()