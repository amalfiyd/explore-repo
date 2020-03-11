def migratoryBirds(arr):
    n = 5
    countArr = [0 for x in range(n)]

    for el in arr:
        countArr[el-1] += 1

    print(countArr)

    maxIdx = -99
    maxVal = -99

    for ix, val in enumerate(countArr):
        if maxVal < val:
            maxVal = val
            maxIdx = ix

    print(maxIdx+1)
    return maxIdx+1

arr = [1,1,2,2,3,3,3,3,3,3,3,4,5,5,5,5,5,5,5,5,5]
arr = []
migratoryBirds(arr)