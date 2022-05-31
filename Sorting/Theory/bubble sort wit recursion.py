def bubble_recursion(array: list, r: int, c: int):
    if r == 0:
        return

    if c < r:
        if array[c] > array[c + 1]:

            temp: int = array[c]
            array[c] = array[c + 1]
            array[c + 1] = temp

        bubble_recursion(array, r, c + 1)

    else:
        bubble_recursion(array, r - 1, 0)


if __name__ == '__main__':

    arr = [4, 3, 2, 1]
    bubble_recursion(arr, len(arr) - 1, 0)
    print(arr)
