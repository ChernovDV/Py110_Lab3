import json


def task():
    filename = "input.json"
    # считать содержимое JSON файла
    with open(filename) as file:
        json_file = json.load(file)

    # записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    gen_exr = sum(value ["contains_improvement_appeals"] for value in json_file)
    return gen_exr


if __name__ == "__main__":
    print(task())
