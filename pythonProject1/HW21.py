txt = open('HW.txt', 'w')
txt.writelines('Change string in text file\nchanging string in list;\nrecord list in file;\n')
txt.close()
txt = open('HW.txt', 'r')
read_txt = txt.readlines()
print(read_txt)
pos1 = int(input('pos1 = '))
del read_txt[pos1]
print(read_txt, '\n')
txt.close()
txt = open('HW.txt', 'w')
txt.writelines(read_txt)
txt.close()

txt = open('HW.txt', 'w')
txt.writelines('Change string in text file\nchanging string in list;\nrecord list in file;\n')
txt.close()
txt = open('HW.txt', 'r')
read_txt = txt.readlines()
print(read_txt)
pos1 = int(input('pos1 = '))
pos2 = int(input('pos2 = '))
read_txt[pos1], read_txt[pos2] = read_txt[pos2], read_txt[pos1]
print(read_txt, '\n')
txt.close()
txt = open('HW.txt', 'w')
txt.writelines(read_txt)
txt.close()

txt = open('HW.txt', 'w')
txt.writelines('Change string in text file\nchanging string in list;\nrecord list in file;\n')
txt.close()
txt = open('HW.txt', 'r')
read_txt = txt.readlines()
print(read_txt)
read_txt.reverse()
print('Reverse\n', read_txt)
txt.close()
txt = open('HW.txt', 'w')
txt.writelines(read_txt)
txt.close()
input()