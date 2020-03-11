def NewYearChaos(q):
    arr = q
    n = len(arr)
    cost = {}
    # Create the cost dictionary
    for el in arr:
        if el not in cost.keys():
            cost[el] = 0

    # Swapping while counting the swap, constraint is at 2 swaps
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # print(arr[j], arr[j+1])
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cost[arr[j+1]] += 1

    # Check if there is a swap > 2
    totalBribes = 0
    for key, val in cost.items():
        totalBribes += val
        if val > 2:
            print('Too chaotic')
            return
    print(totalBribes)
    return

arr = [2,1,5,3,4]
