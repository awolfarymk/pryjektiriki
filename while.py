import random
a = int()
rand = int()
print('Програма генерирует огромные числа из числа которого вы введёте')
chislo = int(input("Введите число\n"))
if 1 <= chislo <= 1000000 : # сгенерироаное число это есть число попыток за которое он угадает написаное число
    while rand != chislo:
        rand = random.randint(1, 1000000)
        a += 1
    print("Число равно: ", a)
else:
    print("Неизвестная ошибка")





