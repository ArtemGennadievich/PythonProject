import os as os_without
import os.path as os_path
import time as t

os_without.makedirs('HW23/D1/D2')
with open('4.txt', 'w') as four:
    four.writelines('something write')
os_without.rename('4.txt', 'HW23/D1/D2/4.txt')
search_list_dir = []
search_list_file = []
search_type = int(input('Что вы хотите найти?\nЕсли файл, нажмите 1\nЕсли папку, нажмите 2\n'))
if search_type == 1:
    search_file = input('Какой файл вам необходимо найти? ') or '4.txt'
if search_type == 2:
    search_dir = input('Какую папку вам необходимо найти? ') or 'D2'
now_position = os_without.getcwd()
for root, dirs, files in os_without.walk(now_position):
    if search_type == 2:
        for i in dirs:
            search_true_dir = False
            if i == search_dir:
                print(f'Папка {i} по пути {os_without.getcwd()} существует')
                print(f'Относительный путь: {os_path.relpath(root)}')
                print(f'Краткая запись пути: {os_path.basename(root)}\\{i}')
                print(f"Время последнего доступа к папке: {os_path.getatime(os_path.join(root, i))}")
                search_list_dir.append(i)

    if search_type == 1:
        for i in files:

            if i == search_file:
                print(f'Файл {i} по пути {os_without.getcwd()} существует')
                print(f'Относительный путь: {os_path.relpath(root)}')
                print(f'Краткая запись пути: {os_path.basename(root)}\\{i}')
                print(f"Время последнего доступа к файлу: {os_path.getatime(os_path.join(root, i))}")
                search_list_file.append(i)
if search_type == 2 and not search_list_dir:
    print(f'Папка {search_dir} по пути {os_without.getcwd()} не существует')
if search_type == 1 and not search_list_file:
    print(f'Файл {search_file} по пути {os_without.getcwd()} не существует')
print('В принципе я сделал универсальную программу для поиска , первую часть кода где создается папка'
      '\nможно было не делать , но все же\n')

for root, dirs, files in os_without.walk(f'{now_position}\Work'):
    for file in files:
        if not os_path.getsize(f'{root}\{file}'):
            if not os_path.exists(f'{now_position}\Work\empty_files'):
                os_without.mkdir(f'{now_position}\Work\empty_files')
                os_without.rename(f'{root}\{file}', f'{now_position}\Work\empty_files\{file}')
            else:
                os_without.rename(f'{root}\{file}', f'{now_position}\Work\empty_files\{file}')
        else:
            print(f"{os_path.relpath(root)}\{file}", os_path.getsize(f'{root}\{file}'), 'bytes')

need_lst_mk = {
    'files': ['one.txt', 'two.txt', 'three.txt'],
    r'files\dir': ['']
}
os_without.makedirs(r'files\dir')
file_txt_lst = []
for dirs, files in need_lst_mk.items():
    if dirs == 'files':
        for file in files:
            file_txt = os_path.join(dirs, file)
            file_txt_lst.append(file_txt)
            open(file_txt, "w").close()
    else:
        file_txt_lst.append(dirs)
print('\n', file_txt_lst)
input()