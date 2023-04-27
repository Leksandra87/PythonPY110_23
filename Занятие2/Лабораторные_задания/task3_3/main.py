def header_footer(fn):
    def wr():
        print('=' * 8)
        f = fn()
        print('=' * 8)
        return f
    return wr

    #  написать декоратор


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
