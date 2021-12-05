data1 = [5, 1, 4, 3, 2, 10, 8]


def bubble_sort(data0):

    swappend = True

    while swappend:
        swappend = False
        for i in range(len(data0)-1):
            if data0[i] > data0[i+1]:
                data0[i], data0[i+1] = data0[i+1], data0[i]
                swappend = True
                print(data0)
    print(data0)


bubble_sort(data1)
