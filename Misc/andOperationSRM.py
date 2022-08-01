def sumofAndPairs(N, A):

    s = 0
    i = 0
    j = N - 1

    while i < j:

        if j > i:
            s += A[i] & A[j]

        if j - i == 1:
            i += 1
            j = N - 1
            continue

        j -= 1

    print(s)


if __name__ == '__main__':
    sumofAndPairs(5, [1, 2, 3, 4, 5])
