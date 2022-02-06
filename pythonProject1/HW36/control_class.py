from HW36 import cylinder


class Control(cylinder.Cylinder):
    def __init__(self, h, r, a=None, b=None):
        super().__init__(h, r, a, b)

    def __add__(self, other):
        return self.volume_cyl() + other.volume_cyl()


control1 = Control(7, 4, 5, 5)
control2 = Control(5, 2, 2, 7)
control3 = Control(3, 9, 15, 16)
control4 = Control(5, 5)
control5 = Control(5, 1)
control1.len_print()
control2.len_print()
control3.len_print()
control4.len_print()
control1.sua_print()
control2.sua_print()
control3.sua_print()
control4.sua_print()
control5.sua_print()
control1.print_per()
control2.print_per()
control3.print_per()
control1.sua_print()
control1.vol_print()
control2.sua_print()
control2.vol_print()
control3.sua_print()
control3.vol_print()
control4.sua_print()
control4.vol_print()
print('*' * 50)
count = []
lst = [control1, control2, control3, control4]
for i in lst:
    count.append(i.volume_cyl())
for i in lst:
    if max(count) == i.volume_cyl():
        result = i.r
print('Окружность с наибольшей площадью: Радиус:', result)
lst1 = [control1, control2, control3]
count1 = []
for i in lst1:
    count1.append(i.perimeter())
for i in lst1:
    if min(count1) == i.perimeter():
        result2 = f"{i.a}, {i.b}"
print('Прямоугольник с наименьшим периметром: Стороны: ', result2)
res1 = control1 + control2
res3 = control4 + control3
res2 = (res3 + res1) / 4
print('Средний объём всех цилиндров: ', res2)

print("\nЕдинственное что не понятно, это то, что в задании либо не правильные ответы , либо использованы другие "
      "экземпляры класса(Если быть точнее, если поставить радиус 8-ку в control3 , то не получится коректный объём"
      " цилиндра, вообщем не совсем понятно) "
      ", ну думаю правильно сделал.")