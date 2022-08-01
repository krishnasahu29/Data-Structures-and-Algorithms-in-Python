# def create_subset(subs: str, string: str):
#     if string == "":
#         print(subs)
#         return
#
#     ch = string[0]
#
#     create_subset(subs + ch, string[1:])
#     create_subset(subs, string[1:])

def create_subset(subs: str, string: str) -> list:
    if string == "":
        ret_str = [subs]
        return ret_str

    ch = string[0]

    left: list = create_subset(subs + ch, string[1:])
    right: list = create_subset(subs, string[1:])

    left.extend(right)
    return left


if __name__ == '__main__':
    print(create_subset("", "abc"))
