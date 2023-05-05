OUTPUT_FILE = "output.txt"


def task():
    s = ''
    with open(OUTPUT_FILE) as file:
        for f in file:
            s += f'{f.strip():>10}' +'\n'
    with open(OUTPUT_FILE, 'w') as rec:
        rec.write(s)
      #  записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
