def selection(a):
    for i in range(0, len(a)):

        c = 0
        m = i
        for k in range(i + 1, len(a)):
            if a[k] < a[m]:
                m = k

        if m != i:
            c += 1
            temp = a[i]
            a[i] = a[m]
            a[m] = temp

        print(c)

mylist = []

n = int(input("Enter no of elements \n"))

for i in range(0, n):
    ele = int(input("Enter element \n"))

    mylist.append(ele)

selection(mylist)
print(mylist)
