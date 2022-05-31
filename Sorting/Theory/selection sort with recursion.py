def selection_recursion(arr: list, length: int, i: int, maximum: int):

    if length == 0:
        return

    if i < length:
        if arr[i] > arr[maximum]:
            selection_recursion(arr, length, i + 1, i)

        else:
            selection_recursion(arr, length, i + 1, maximum)

    else:
        temp = arr[maximum]
        arr[maximum] = arr[length - 1]
        arr[length - 1] = temp

        selection_recursion(arr, length - 1, 0, 0)


if __name__ == '__main__':

    array = [5, 4, 8, 2, 1]
    selection_recursion(array, len(array), 0, 0)
    print(array)
