import sys


def min_moves(nums):
    median = sorted(nums)[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print('Использование: python ./task4/task4.py ./task4/numbers.txt')
            sys.exit(1)

        filepath = sys.argv[1]

        with open(filepath, 'r') as f:
            nums = [int(line.strip()) for line in f]
        print(min_moves(nums))
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
