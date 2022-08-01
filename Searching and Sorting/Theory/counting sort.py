from collections import defaultdict


def counting_sort(A):
    B, C = [], defaultdict(list)
    key = lambda x: x
    for x in A:
        C[key(x)].append(x)

    for k in range(min(C), max(C) + 1):
        B.extend(C[k])

    return B


if __name__ == '__main__':
    print(counting_sort([5, 2, 8, 3, 9]))
