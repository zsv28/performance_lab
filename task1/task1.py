def circular_array(n, m):
    """
    Генерирует порядок элементов в круговом массиве размером n с шагом m,
    начиная с первого элемента и возвращаясь к началу.
    """
    # Начинаем с первого элемента
    current = 1
    path = [current]

    # Перемещаемся по массиву до тех пор, пока не вернемся к начальному элементу
    while True:
        current = (current + m - 2) % n + 1

        if current == 1:  # Если вернулись в начало, завершаем цикл
            break
        path.append(current)

    return path


def main():
    # Запрашиваем ввод у пользователя
    try:
        n = int(input('Введите размер кругового массива (n): '))
        m = int(input('Введите длину интервала (m): '))

        if n <= 0 or m <= 0:
            print('n и m должны быть положительными числами')
            return

        path = circular_array(n, m)
        print(''.join(map(str, path)))
    except ValueError:
        print('Входные данные должны быть целыми числами')


if __name__ == "__main__":
    main()
