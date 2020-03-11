def twoDArray(arr):
    rowLen, colLen = len(arr), len(arr[0])
    maxSum = -9999
    maxRow, maxCol = -99, -99
    for row in range(rowLen - 2):
        for col in range(colLen - 2):
            total, rowIx, colIx = peekHourGlass(arr, row, col)
            if maxSum < total:
                maxSum = total
                maxRow, maxCol = rowIx, colIx

    return peekHourGlass(arr, maxRow, maxCol)[0]

def peekHourGlass(arr, rowIx, colIx):
    total = 0
    skipCount = 0
    for row in range(rowIx, rowIx+3):
        for col in range(colIx, colIx+3):
            if skipCount != 3 and skipCount != 5:
                total += arr[row][col]
            skipCount += 1
    return (total, rowIx, colIx)




arr = [[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]]

temp = twoDArray(arr)