import json


def task():
    filename = "input.json"
    # считать содержимое JSON файла
    with open(filename) as file:
        json_file = json.load(file)

        # найти максимальный элемент по ключу score
        x = max(json_file, key = lambda value:value["score"])
    return x


if __name__ == "__main__":
    print(task())
