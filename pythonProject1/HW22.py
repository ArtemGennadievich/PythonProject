with open('hw22.txt', 'w') as wrt:
    wrt.writelines('первая строка\nстрока номер два\nтретья строка\n4 строка')
with open('hw22.txt', 'r') as wrt:
    wrt_ch_2 = wrt.readlines()
    ch = -1
    res_sim = 0
    for i in wrt_ch_2:
        ch += 1
        print(i, end=' ')
        print(len(wrt_ch_2[ch]), 'симв.', len(i.split()), 'сл.')
print(len(wrt_ch_2), 'стр.')

with open('hw22_file1.txt', 'w') as write:
    write.writelines('First file.')
with open('hw22_file2.txt', 'w') as write2:
    write2.writelines('Second file.')
with open('hw22_file2.txt', 'r') as read2, open('hw22_file1.txt', 'r') as read, open('hw22_file3.txt', 'w') as all_write:
    all_write.writelines([i for i in read2] + [i for i in read])

input()
