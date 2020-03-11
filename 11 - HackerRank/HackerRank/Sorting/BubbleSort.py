def bubblesort(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter += 1

    return (counter, arr[0], arr[len(arr)-1])

temp = [4,3,1,2,5,8,9]
print(bubblesort(temp))