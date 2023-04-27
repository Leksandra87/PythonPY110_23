def check_iter(fn):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args):
            try:
                iter(arg)
            except TypeError:
                raise TypeError(f'Объект номер {index + 1} не является итерируемым')
        for key, kwarg in kwargs.items():
            try:
                iter(kwarg)
            except TypeError:
                raise TypeError(f'Объект  по ключу "{key}" не является итерируемым')
        result = fn(*args, **kwargs)
        return result

    return wrapper


@check_iter
def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)


@check_iter
def print_args(*args):
    print(type(args), args)


if __name__ == "__main__":
    print_args("adg", [1, 2, 3])
    print_kwargs(a=[], b='', c=4)
    # Write your solution here

    pass
