data = [5, 1, 4, 3, 2, 10, 8]
data_best = [1, 2, 3, 4, 5, 8, 10]
data_worst = [10, 8, 5, 4, 3, 2, 1]

def selection_sort(data):
    marker = 0
    steps = 0
    while marker < len(data):
        steps += 1
        min_index = marker
        for i in range(marker, len(data)):
            steps += 1
            if data[marker] > data[i]:
                if data[i] < data[min_index]:
                    min_index = i
        data[marker], data[min_index] = data[min_index], data[marker]
        print(data)
        marker+=1

    print(data)
    print(steps)


# 35 in data, data_best, data_worst
selection_sort(data_worst)