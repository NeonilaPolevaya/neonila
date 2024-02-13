# TODO решите задачу
import json


filename = 'input.json'


def task() -> float:
    with open(filename) as file:
        data = json.load(file)
    list_val = [dict["score"] * dict["weight"] for dict in data]
    value = sum(list_val)
    return round(value, 3)


print(task())

