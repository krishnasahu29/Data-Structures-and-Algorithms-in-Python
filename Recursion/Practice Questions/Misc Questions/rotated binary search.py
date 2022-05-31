"""
if arr[start] <= arr[mid]

    if arr[start] <= key <= arr[mid]
        end = mid - 1

    else
        start = mid + 1

    if arr[end] <= key <= arr[mid]
        start = mid + 1

    else
        end = mid - 1

"""


def recursion(arr: list, target, s, e):
    if s > e:
        return -1

    m = int(s + (e - s) / 2)

    if arr[m] == target:
        return m

    if arr[s] <= arr[m]:
        if arr[s] <= target <= arr[m]:
            return recursion(arr, target, s, m - 1)

        else:
            return recursion(arr, target, m + 1, e)

    if target <= arr[e] <= arr[m]:
        return recursion(arr, target, m + 1, e)

    return recursion(arr, target, s, m - 1)


if __name__ == '__main__':

    arr = [5, 6, 7, 8, 9, 1, 2, 3]
    print(recursion(arr, 4, 0, len(arr) - 1))
