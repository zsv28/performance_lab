def determine_point_position(
        circle_center_x, circle_center_y, radius, point_x, point_y):
    """
    Определяет положение точки относительно окружности:
    0 - точка лежит на окружности
    1 - точка внутри окружности
    2 - точка снаружи окружности.
    """
    # Вычисляем квадрат расстояния от точки до центра окружности
    distance_squared = (point_x - circle_center_x) ** 2 + (
            point_y - circle_center_y) ** 2

    # Вычисляем квадрат радиуса (для избежания погрешностей при сравнении)
    radius_squared = radius ** 2

    # Определяем положение точки
    if abs(
            distance_squared - radius_squared) < 1e-10:  # Погрешность
        return 0  # На окружности
    elif distance_squared < radius_squared:
        return 1  # Внутри окружности
    else:
        return 2  # Снаружи окружности


def main():
    try:
        # Запрашиваем пути к файлам у пользователя
        circle_file_path = input(
            'Введите путь к файлу с параметрами окружности: ')
        points_file_path = input('Введите путь к файлу с координатами точек: ')

        # Читаем данные об окружности
        with open(circle_file_path, 'r') as circle_file:
            # Первая строка - координаты центра
            center_coords = circle_file.readline().strip().split()
            circle_center_x = float(center_coords[0])
            circle_center_y = float(center_coords[1])

            # Вторая строка - радиус
            radius = float(circle_file.readline().strip())

        # Читаем координаты точек
        with open(points_file_path, 'r') as points_file:
            points = []
            for line in points_file:
                if line.strip():  # Проверяем, что строка не пустая
                    coords = line.strip().split()
                    points.append((float(coords[0]), float(coords[1])))

        # Определяем положение каждой точки и выводим результат
        for point_x, point_y in points:
            position = determine_point_position(
                circle_center_x, circle_center_y, radius, point_x, point_y)
            print(position)

    except FileNotFoundError:
        print('Ошибка: один из указанных файлов не найден')
    except ValueError:
        print('Ошибка: некорректный формат данных в файлах')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    main()
