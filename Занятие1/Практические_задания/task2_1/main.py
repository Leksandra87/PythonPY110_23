if __name__ == "__main__":
    str_ = "1q2w3e4r5t6y"
    chars = list(filter(str.isalpha, str_))  # переписать с помощью filter

    print("".join(chars))
