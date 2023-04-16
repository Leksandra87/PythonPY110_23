from itertools import repeat


def task():
    a = 10
    for num in range(4):  #  повторить переменную a 4 раза
        print(next(repeat(a)))


if __name__ == "__main__":
    task()
