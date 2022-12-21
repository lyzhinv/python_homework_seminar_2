# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
while True:
    try:

        import random

        n = int(input('Введите количество монеток: '))

        m = []
        for item in range(n):
            random_number = round(random.uniform(0, 1), 0)
            m.append(int(random_number))

        print(f'{n} -> {m}')

        i = 0
        count1 = count2 = 0
        while i < n:
            if m[i] == 1:
                count1 += 1
            else:
                count2 += 1
            i += 1
        if count1 > count2:
            print(f'Необходимо перевернуть {count2} монет(ы)')
            break
        else:
            print(f'Необходимо перевернуть {count1} монет(ы)')
            break
    
    except:
        print('Необходимо ввести число')