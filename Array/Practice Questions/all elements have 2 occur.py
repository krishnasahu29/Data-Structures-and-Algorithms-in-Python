class array:

    def find_element(self, num):
        num_sorted = sorted(num)

        for i in range(len(num_sorted) - 2):
            if num_sorted[i] is not num_sorted[i+1] and num_sorted[i+1] is not num_sorted[i+2] and num_sorted[i] is not num_sorted[i+2]:
                return num_sorted[i+1]


if __name__ == '__main__':
    arr = array()
    print(arr.find_element([1, 1, 2, 2, 3, 4, 4]))
