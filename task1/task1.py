def circular_array(n, m):
    """
    Находит последовательность индексов в круговом массиве размера n с шагом m.
    """
    i = 1
    # Ограничиваем размером массива
    for _ in range(n):
        yield i
        i = (i + m - 2) % n + 1
        if i == 1:
            break


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите размер кругового массива (n): '))
            m = int(input('Введите длину интервала (m): '))

            if n > 0 and m > 0:
                print(
                    'Полученный путь:', ''.join(
                        map(str, circular_array(n, m)))
                )
                break
            print('n и m должны быть положительными числами.')
        except ValueError:
            print('Введите два целых числа.')
