def calculateOutputValues(medals):
    res = [max(medals)]

    c_1, c_2 = 0, 0
    for i in medals:
        if i >= 1:
            c_1 += 1

        if i == 0:
            c_2 += 1

    res.extend([c_1, c_2])
    res.append(medals[-1] + medals[-2] + medals[-3])

    return res


if __name__ == '__main__':
    print()
