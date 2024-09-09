print('Вам нужно ввести три целых числа.')

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
# Надеюсь, что так можно сформулировать это условие, тем более, что оно работает.
# Если нет, то if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')