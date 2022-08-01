def hamming(s1: str, s2: str) -> int:

    c = 0
    for a, b in zip(s1, s2):
        if a != b:
            c += 1

    return c


if __name__ == '__main__':
    print(hamming('abc', 'bbc'))
