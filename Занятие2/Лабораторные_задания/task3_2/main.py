def min_len_check(fn):
    def wrapper(str_):
        if len(str_) > 10:
            res_ = fn(str_)
            return res_
        else:
            raise ValueError("Строка слишком короткая")

    #  записать обертку для исходной функции

    return wrapper


#  задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    return print(f'Строка {str_arg} подходит')


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
