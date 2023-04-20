def positive_check(fn):
    def wrapper(arg):
        if arg > 0:
            result = fn(arg)
        else:
            raise ValueError("Аргумент функции не является положительным числом")

        #  написать проверку положительности аргумента arg

        return result

    return wrapper


#  задекорировать функцию
@positive_check
def some_func(num: int):
    s = 2 ** num
    return print(s)


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
