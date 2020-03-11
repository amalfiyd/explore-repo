def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        print(arr)
    return arr

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
            print(arr)

    return arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
        merge(arr, L, R)

    return arr

def merge(arr, L, R):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [9,1,2,4,6,1,8,4,1,2,8,9]
# print("Selection Sort", selectionSort(arr))
# print("Insertion Sort", insertionSort(arr))
# print("Bubble Sort", bubbleSort(arr))
# print("Merge Sort", mergeSort(arr))
# print("Quick Sort", quickSort(arr, 0, len(arr)-1))