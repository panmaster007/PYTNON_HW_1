# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

orel = int(input('Введите количество монет лежащих орлом вверх: '))
reshka = int(input('Введите количество монет лежащих решкой вверх: '))

if orel > reshka:
    print(f"нужно перевернуть минимум {reshka} монет(ы)")
else:
    print(f"нужно перевернуть минимум {orel} монет(ы)")
