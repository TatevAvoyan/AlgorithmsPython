data = [5, 1, 4, 3, 2, 10, 8]
data_best = [1, 2, 3, 4, 5, 8, 10]
data_worst = [10, 8, 5, 4, 3, 2, 1]

def bubble_sort(data):
    steps = 0
    swappend = True
    while swappend:
        steps += 1
        swappend = False
        for i in range(len(data)-1):
            steps += 1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swappend = True
                print(data)
    print(data)
    print(steps)

# 28 in data, 7 in data_best, 49 in data_worst
bubble_sort(data_worst)