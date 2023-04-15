# Требуется определить, можно ли от шоколадки размером NxM долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника)
# Пример: 1  2  4  -> yes
#         3  2  1  -> no


x = int(input('Введите количество долек по одной стороне шоколадки: '))
y = int(input('Введите количество долек по второй стороне шоколадки: '))
d = int(input('Введите количество долек которые вы хотите отломить: '))

if (d % x == 0 or d % y == 0) and d < x * y:
   print('Да, так можно поделить!')
else:
   print('Нет, такой расклад не пойдёт!')
