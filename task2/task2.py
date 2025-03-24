import sys


def point_position(circle_x, circle_y, circle_r, point_x, point_y):
    """
    Определяет положения точки относительно окружности.
    """
    distance = (circle_x - point_x) ** 2 + (circle_y - point_y) ** 2
    radius = circle_r ** 2

    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def is_valid_number(num):
    return (10 ** -38 <= num <= 10 ** 38) or num == 0


if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print(
                'Использование: python ./task2/task2.py ./task2/circle.txt '
                './task2/points.txt'
            )
            sys.exit(1)

        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            circle_x, circle_y = map(float, lines[0].split())
            circle_r = float(lines[1].strip())

            if not all(
                    is_valid_number(val) for val in
                    [circle_x, circle_y, circle_r]):
                raise ValueError(
                    'Параметры окружности вне допустимого диапазона.')

        with open(sys.argv[2], 'r') as f:
            points = []
            for line in f:
                if not line.strip():
                    continue

                x, y = map(float, line.split())
                if not (is_valid_number(x) and is_valid_number(y)):
                    raise ValueError(
                        f'Координаты {x}, {y} вне допустимого диапазона.')
                points.append((x, y))

            if not 1 <= len(points) <= 100:
                raise ValueError(
                    f'Недопустимое количество точек: {len(points)}')

        # Определяем и выводим положение каждой точки
        for x, y in points:
            print(point_position(circle_x, circle_y, circle_r, x, y))

    except FileNotFoundError:
        print('Один из файлов не найден.')
