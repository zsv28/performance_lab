import json


def fill_report_structure(structure, values_dict):
    """
    Рекурсивно заполняет структуру отчета значениями тестов.
    """
    if isinstance(structure, dict):
        # Если в элементе есть id, заполняем значение
        if 'id' in structure:
            test_id = structure['id']
            # Заполняем значение, если оно есть в values_dict
            if test_id in values_dict:
                structure['value'] = values_dict[test_id]

        # Рекурсивно обрабатываем все вложенные элементы
        for key, value in structure.items():
            if isinstance(value, (dict, list)):
                structure[key] = fill_report_structure(value, values_dict)

    elif isinstance(structure, list):
        # Обрабатываем каждый элемент списка
        for i in range(len(structure)):
            structure[i] = fill_report_structure(structure[i], values_dict)

    return structure


def main():
    try:
        # Запрашиваем пути к файлам у пользователя
        values_file = input('Введите путь к файлу values.json: ')
        tests_file = input('Введите путь к файлу tests.json: ')
        report_file = input('Введите путь к файлу report.json: ')

        # Загружаем данные из файлов
        with open(values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
            # Создаем словарь для быстрого поиска по id
            values_dict = {item['id']: item['value'] for item in
                           values_data.get('values', [])}

        with open(tests_file, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)

        # Создаем копию структуры tests_data, чтобы не изменять оригинал
        report_data = json.loads(json.dumps(tests_data))

        # Заполняем отчет значениями
        report_data = fill_report_structure(report_data, values_dict)

        # Записываем результат в файл report.json
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)

        print(f'Отчет успешно сформирован и записан в файл {report_file}')

    except FileNotFoundError as e:
        print(f'Ошибка: Файл не найден - {e}')
    except json.JSONDecodeError as e:
        print(f'Ошибка при разборе JSON: {e}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    main()
