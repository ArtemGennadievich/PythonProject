name = (input('What is your name? '))
age = int(input('How old are you? '))
country = (input('Where are u live? '))
print('This is ' + name)
print('It is ', age)
print('He lives in ' + country)

ch = int(input('Решите пример: 4 * 100 - 54 \nВаш ответ: '))
print('Правильный ответ: 346 \nВаш ответ: ', ch)

num = int(input('Введите целое число : '))
if (num % 2) == 0:
    print('Число ', num, '- четное')
else:
    print('Число ', num, '- нечетное')
input()
