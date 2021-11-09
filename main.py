data = [5, 1, 4, 3, 2, 10, 8]
data_best = [1, 2, 3, 4, 5, 8, 10]
data_worst = [10, 8, 5, 4, 3, 2, 1]

def insertion_sort(data):

    steps = 0
    for i in range(1, len(data)):
        steps += 1
        while data[i-1] > data[i] and i > 0:
            steps += 1
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1
        print(data)

    print(data)
    print(steps)

# 14 in data, 6 in data_best, 27 in data_worst
insertion_sort(data_worst)
