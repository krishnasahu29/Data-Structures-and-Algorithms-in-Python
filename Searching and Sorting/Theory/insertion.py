class Insertion:
    def __init__(self, mylist):
        self.mylist = mylist

    def sort(self, mylist):
        c = 0
        for index in range(1, len(mylist)):

            temp = mylist[index]
            pos = index

            while pos > 0 and mylist[pos - 1] > temp:
                c += 1
                mylist[pos] = mylist[pos - 1]
                pos -= 1

            mylist[pos] = temp

        print(c)


if __name__ == '__main__':

    mylist = []

    n = int(input("Enter no of elements \n"))

    for i in range(0, n):
        ele = int(input("Enter element \n"))

        mylist.append(ele)

    insert = Insertion(mylist)
    insert.sort(mylist)
    print(mylist)
