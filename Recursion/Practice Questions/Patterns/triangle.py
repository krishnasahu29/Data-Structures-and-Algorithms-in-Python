def triangle(r: int, c: int):
    if r == 0:
        return

    if c < r:
        triangle(r, c + 1)
        print("*", end=" ")

    else:
        triangle(r - 1, 0)
        print()


if __name__ == '__main__':

    triangle(4, 0)
