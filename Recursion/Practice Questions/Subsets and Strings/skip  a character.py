def skip_character(s, string: str, char: str):

    if string == "":
        print(s)
        return

    if string[0] == char:
        skip_character(s, string[1:], char)

    else:
        skip_character(s + string[0], string[1:], char)


if __name__ == '__main__':

    s = ""
    string = "baccad"
    skip_character(s, string, "a")
