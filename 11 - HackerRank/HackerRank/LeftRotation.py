def leftRotation(a,d):
    rotNum = len(a) - d
    firstEl = a[:-rotNum]
    lastEl = a[-rotNum:]
    return lastEl + firstEl

a = [1,2,3,4,5]
d = 2

temp = leftRotation(a,d)