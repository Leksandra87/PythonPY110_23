def check_int(fn):
    def wrap_(*args):
        a = True
        for i in args:
            if type(i) != int:
                a = False
        if a:
            return fn(*args)
        else:
            raise 'Эта функция работает только с натуральными числами'
    return wrap_
@check_int
def sum_(*args):
    s = sum([i for i in args])
    return print(s)





if __name__ == "__main__":

    sum_(1, 2, 4, 5, [])
    # Write your solution here
    pass
