# TODO решите задачу
import json


filename = 'input.json'


def task() -> float:
    with open(filename) as file:
        data = json.load(file)
    value = 0
    for dict in data:
        value += dict["score"] * dict["weight"]
    return round(value, 3)



print(task())
