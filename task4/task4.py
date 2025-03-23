import sys


def min_moves_to_equal(nums):
    """
    Вычисляет минимальное количество ходов,
    необходимых для приведения всех элементов массива к одному числу.
    """
    nums.sort()  # Сортируем массив
    median = nums[len(nums) // 2]  # Находим медиану

    # Вычисляем суммарное количество шагов, необходимых для приведения всех
    # чисел к медиане
    moves = sum(abs(num - median) for num in nums)

    return moves


if __name__ == "__main__":
    filename = input('Введите имя файла: ')

    try:
        # Читаем числа из файла
        with open(filename, 'r') as file:
            nums = [int(line.strip()) for line in file]

        # Вычисляем минимальное количество ходов и выводим результат
        print(min_moves_to_equal(nums))
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
