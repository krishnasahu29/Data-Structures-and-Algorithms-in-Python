def create_subset_ascii(subs: str, string: str):

    if string == "":
        print(subs)
        return

    ch = string[0]

    create_subset_ascii(subs + ch, string[1:])
    create_subset_ascii(subs, string[1:])
    create_subset_ascii(ord(ch), string[1:])


if __name__ == '__main__':
    print(create_subset_ascii('', 'abc'))
