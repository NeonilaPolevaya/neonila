# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME) as input_f:
        reader = csv.DictReader(input_f)
        for row in reader:
            data.append(row)
        # TODO считать содержимое csv файла

      # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output_f:
        json.dump(data, output_f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
