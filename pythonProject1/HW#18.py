import re
test = '123456@i.ru,123_456@ru.name.ru, ' \
       'login@i.ru,логин-1@i.ru,login.3-67@i.ru, 1login@ru'
reg = r'[\w\.-]+[@][\w+\.?\w]+'
print(re.findall(reg, test))
input()