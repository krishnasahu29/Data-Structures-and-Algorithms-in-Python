def skip_string(s, string: str, char: str):

    sub_len = len(char)

    if string == "":
        print(s)
        return

    if string[0:sub_len] == char:
        skip_string(s, string[sub_len:], char)

    else:
        skip_string(s + string[0], string[sub_len:], char)


if __name__ == '__main__':

    s = ""
    string = "baccacd"
    skip_string(s, string, "ac")
