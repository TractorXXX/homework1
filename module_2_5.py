def get_matrix(n, m, value):
    matrix = []    #
    for i in range(n):    # Создает список строк, каждая из которых будет являтся списком столбцов
        matrix_1 = []     # Создаем пустой список столбцов
        for j in range(m):    # Создает список столбцов
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix

n1 = int(input('Введите количество строк в матрице: '))
m1 = int(input('Введите количество столбцов в матрице: '))
value1 = int(input('Введите значение элемента матрицы: '))

if n1 > 0 and m1 >0 and value1 > 0:    # При аргументах со значением 0 или меньше, будет возвращаться пустой список
    result = get_matrix(n1, m1, value1)
    print(result)
else:
    result = []
    print(result)