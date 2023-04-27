def pairwise1(iterable):
    for i in range(len(iterable) - 1):
        x = list(zip(iterable[i], iterable[i + 1]))
        yield x


def task(arg):
    s = 0
    for pair in pairwise1(arg):
        s += (sum(pair[0]) ** 2 + sum(pair[1]) ** 2) ** 0.5
    print(s)


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
task(pts)
