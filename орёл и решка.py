import random
print('Программа считает сколько выпадет орёл, а сколько решка за 100 попыток')
a = int()
b = int()
while a + b != 100 :
    a = random.randint(1, 100)
    b = random.randint(1, 100)
print('Орёл выпал ', a, 'раз\n', 'Решка выпал', b)







