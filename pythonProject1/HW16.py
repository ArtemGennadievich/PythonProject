str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
a = 0
srt2 = ''
while a < len(str1):
    if str1[a] == 'N':
        srt2 = srt2 + 'P'
        if a == 9:
            srt2 = srt2[:9:] + "N"
    else:
        srt2 = srt2 + str1[a]
    a += 1
print(f'str1 = {str1}')
print(f'str2 = {srt2}\n')

s = '0123456789'
s2 = s.replace('4', '')
print(f's = {s}')
print(f's2 = {s2}')

g = '012345363738494'
print(f'\ns = 012345363738494\ns2 = {g.replace("3", "")}\n')


def dvoich(chislo):
    print('->', chislo)
    stepeni_dvoyki = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    ind = 0
    dv_kod = []
    if chislo == 0:
        dv_kod.append(0)
    elif chislo == 1:
        dv_kod.append(1)
    for i in stepeni_dvoyki:
        if i < chislo:
            ind += 1
    t = stepeni_dvoyki[:ind]
    index = -1
    for i in range(len(t)):
        if chislo >= t[index]:
            chislo = chislo - t[index]
            dv_kod.append(1)
        else:
            dv_kod.append(0)
        index += -1

    print(dv_kod)

dvoich(53)
dvoich(145)
dvoich(255)
dvoich(0)

input()
