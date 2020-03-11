def drawingBook(n,p):
    if p <= n // 2:
        # start from left
        print('left')
        counter = 0
        curPage = 1
        while curPage < p:
            curPage += 2
            counter += 1
    else:
        # start from right
        print('right')
        counter = 0
        curPage = n + 1 if n % 2 == 0 else n
        while p < curPage - 1:
            curPage -= 2
            counter += 1

    return counter

n = 7
p = 4

temp = drawingBook(n,p)
print(temp)