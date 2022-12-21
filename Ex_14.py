# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5 - 1 2 4
# 17 - 1 2 4 8 16

while True:
    try:

        N = int(input("Введите число "))
        result = 1

        print(f'{N} ->', end = ' ')

        while result <= N:
            print(result, end = ' ')
            result *= 2
        break
    except:
        print('Ошибка! Необходимо ввести число')