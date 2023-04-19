def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(len(x) for x in list_words)  #  записать выражение-генератор


if __name__ == "__main__":
    print(task())
