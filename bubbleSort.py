# 1 - Comenzar a hacer elementos adyacentes
# 2 - Repetir hasta tener una pasada completa sin ningun swap


def bubbleSort(array):
    n = len(array)
    for i in range(n):
        # print(array)
        for j in range(0, n-i-1):
            print(n-i-1)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [1, 33, 2, 4322, 21, 1331, 90]
bubbleSort(array)
# print(array)

# for i in range(len(array)):
#     print("%d" % array[i])
