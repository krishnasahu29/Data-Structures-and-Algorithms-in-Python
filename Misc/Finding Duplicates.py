def repeat_num(arr, n):
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

    for i in range(0, n):
        if (arr[i] / n) >= 2:
            print(i, end=", ")


# Driver code
if __name__ == '__main__':
    arr = [2, 7, 1, 4, 1, 7, 8, 2, 8]
    n = len(arr)

    repeat_num(arr, n)
