def deliteli(k):    # Данная функция находит делители числа
    spisok_deliteley = []
    for i in range(3, k + 1):
        if n % i == 0:
            spisok_deliteley.append(i)
        else:
            continue
    return spisok_deliteley
#---------------------------------------------------

def pary_delitel(m):    # Функция строит список пар
    pary_deliteley = []
    m_2 = m // 2 + 1
    for i in range(1, m_2):
        if i != m - i:   # Удаляем пару одинаковых чисел, т.к. это делитель
            para_del = [i, m - i]
            pary_deliteley.append(para_del)
        else:
            break
    return pary_deliteley
#----------------------------------------------------

def parol(l):    # Функция переводит список в строку пароля
    parol_str = str()
    for i in l:
        parol_str_1 = str(i[0]) + str(i[1])
        parol_str = parol_str + parol_str_1
    return parol_str
#----------------------------------------------------

import random
n = random.randint(3, 20)    # Имитируем случайное число из первой вставки
print('Число из первой вставки: ', n)

spisok_delit = deliteli(n)    # Находим делители этого числа

pary_del = []

for i in spisok_delit:    # Создаем общий список пар от всех делителей и сортируем его
    pary = pary_delitel(i)
    pary_del = pary_del + pary
    pary_del.sort()

result = parol(pary_del)    # Вычисляем пароль
print('Нужный пароль: ', result)





