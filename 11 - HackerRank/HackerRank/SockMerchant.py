def sockMerchant(n, ar):
    countDict = {}
    for el in ar:
        if el in countDict.keys():
            countDict[el] += 1
        else:
            countDict[el] = 1

    pairCount = 0
    for key, value in countDict.items():
        pairCount += value // 2

    print(countDict)
    return int(pairCount)

ar = [10,20,20,10,10,30,50,10,20]
n = len(ar)
pairCount = sockMerchant(n, ar)
print(pairCount)