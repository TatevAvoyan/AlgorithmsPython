data = [5, 1, 4, 3, 2, 10, 8]

def bubble_sort(data):
    swappend = True
    while swappend:
        swappend = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swappend = True
                print(data)
    print(data)


bubble_sort(data)