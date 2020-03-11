def electronicShops(keyboards, drives, b):
    maxCombVal = -1

    for k in keyboards:
        for d in drives:
            if k+d <= b and maxCombVal <= k+d:
                maxCombVal = k+d

    return maxCombVal
