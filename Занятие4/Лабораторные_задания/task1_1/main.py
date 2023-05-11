import json
import re
OUTPUT_FILE = "output.json"
BOOKS_FILE = "books.md"
BOOK_REGEX =  r'(?P<position>\d+)\.\s\[(?P<book>.+?)\]\((?P<book_url>.+?)\) by\b\s(?P<author>.+?)\s\((?P<recommended>.+?%).+?\((?P<cover_url>.+?)\).+?\"(?P<description>.+?)\"'  #   записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)
    # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    li = []
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))
            li.append(book.groupdict())
        li.sort(key=lambda x: x["recommended"])
    with open(OUTPUT_FILE, "w") as f:
        json.dump(li, f, indent=4, ensure_ascii=False)




if __name__ == '__main__':
    task()


# https://regex101.com/