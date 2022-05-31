def recursion(array, target, index):
    indices_list = []

    if index == len(array):
        return indices_list

    if array[index] == target:
        indices_list.append(index)

    ans_list = recursion(array, target, index + 1)
    indices_list.extend(ans_list)

    return indices_list


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 4, 5]
    print(recursion(arr, 4, 0))
    