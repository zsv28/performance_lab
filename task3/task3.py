import json
import sys


def fill_report(tests_data, values):
    """
    Заполняет отчет значениями по id.
    """
    for test in tests_data.get('tests', []):
        if 'id' in test and test['id'] in values:
            test['value'] = values[test['id']]

        if 'values' in test:
            fill_report(
                {'tests': test['values']},
                values)

    return tests_data


if __name__ == '__main__':
    try:
        if len(sys.argv) != 4:
            print(
                'Использование: python ./task3/task3.py ./task3/values.json '
                './task3/tests.json ./task3/report.json'
            )
            sys.exit(1)

        values_file, tests_file, report_file = sys.argv[1], sys.argv[2], \
            sys.argv[3]

        with open(values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
            values_dict = {item['id']: item['value'] for item in
                           values_data.get('values', [])}

        with open(tests_file, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)

        report_data = fill_report(
            json.loads(json.dumps(tests_data)),
            values_dict
        )

        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)

        print(f'Отчет {report_file} успешно сформирован.')

    except FileNotFoundError:
        print('Один из файлов не найден.')
