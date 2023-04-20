def count(start_number: float = 1, step: float = 1):
    num = start_number
    if num == int(num):
        yield int(num)
    while True:
        num += step
        if num == int(num):
            yield int(num)
      #  написать функцию-генератор возвращающую целые числа


if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
