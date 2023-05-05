INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:
        for f in file:
            print(f.rstrip())
#  открыть указатель на файл
          #  файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
