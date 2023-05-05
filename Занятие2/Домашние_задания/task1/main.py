def geo_prog():
    num = 1
    q = 2
    while True:
        yield num
        num = num * q


if __name__ == "__main__":
    d = geo_prog()
    for _ in range(10):
        print(next(d))
    # Write your solution here
    pass
