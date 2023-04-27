import random
from string import ascii_lowercase, ascii_uppercase, digits


def gen_cod(n=8):
    while True:
        a = ''.join(random.sample((ascii_lowercase + ascii_uppercase + digits), n))
        yield a


if __name__ == "__main__":
    g = gen_cod()
    for _ in range(5):
        print(next(g))
