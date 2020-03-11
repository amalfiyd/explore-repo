def minSwaps(arr):
    n = len(arr)
    arrPos = [(x,y) for x,y in enumerate(arr)]
    arrPos.sort(key=lambda el: el[1])
    vis = {i: False for i in range(n)}

    swaps = 0
    for i in range(n):
        if vis[i] or arrPos[i][0] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True

            j = arrPos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            swaps += (cycle_size - 1)
    return swaps