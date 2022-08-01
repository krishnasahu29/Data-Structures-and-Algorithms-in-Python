# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

def printDups(string: str) -> None:
    count = {}

    for i in string:

        if i == ' ':
            continue

        if i not in count.keys():
            count[i] = 1

        else:
            count[i] += 1

    for i in count.keys():
        if count[i] > 1:
            print("{}: count = {}".format(i, count[i]))


if __name__ == '__main__':
    printDups('geeks for geeks')
