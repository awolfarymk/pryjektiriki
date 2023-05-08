from math import sqrt
# Эта программа будет считать корни квадратного уравнения
print('Эта програма считает корни квадратного уровнения')
a = int(input("Введите первый коэффициет\n"))
b = int(input("Введите второй коэфицент\n"))
c = int(input("Введите свободный член\n"))
# формула дескриминанта
d = b*b - 4*a*c
if d>=1:
    x1 = -b + sqrt(d) / 2*a
    x2 = -b - sqrt(d) / 2*a
    print('\t\t\tD = ', d)
    print("\t\t\tx1 = ", x1)
    print("\t\t\tx2 = ", x2)
elif d == 0:
    x = -b/2 * a
    print("\t\t\tD = ", D)
    print('\t\t\tx = ', x)
else:
    print('\t\t\tне имеет корней')
