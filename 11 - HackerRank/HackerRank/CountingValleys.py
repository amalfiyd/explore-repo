def countingValleys(n, s):
    touchZero = 0
    curLevel = 0
    for el in s:
        if el == 'U' and curLevel == -1:
            touchZero += 1
        curLevel += 1 if el == 'U' else -1

    return touchZero

s = [x for x in 'UDDDUDUU']
n = len(s)

temp = countingValleys(n,s)
