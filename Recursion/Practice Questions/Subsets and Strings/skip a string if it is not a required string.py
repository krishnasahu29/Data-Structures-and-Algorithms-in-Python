def skip_string_not_req(s, string: str, char: str):

    sub_len = len(char)

    if string == "":
        print(s)
        return

    if string[0:sub_len] == char:
        skip_string_not_req(s + char, string[sub_len:], char)

    else:
        skip_string_not_req(s, string[1:], char)


if __name__ == '__main__':

    skip_string_not_req("", "baccacd", "ac")
