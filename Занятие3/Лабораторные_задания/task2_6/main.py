import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
        s_data = sorted(json_data, key=lambda x: x["length"])

    return s_data  # отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))
    with open('new.json', 'w') as n:
        json.dump(data, n, indent=4, ensure_ascii=False)

    #  дополнительно записать отсортированный список в JSON файл
