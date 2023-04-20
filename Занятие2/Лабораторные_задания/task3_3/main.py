def header_footer():
    print('=' * 8)


    #  написать декоратор


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
