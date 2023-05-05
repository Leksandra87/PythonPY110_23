import json


def task():
    filename = "input.json"
    with open(filename) as f:
        d = json.load(f)

    #  считать содержимое JSON файла

    return max(d, key=lambda x: x['score'])  # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
