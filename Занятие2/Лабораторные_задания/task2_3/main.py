def pow_gen(base: int):
    f = 0
    while True:
        num = base ** f
        f += 1
        yield num
      #  записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
