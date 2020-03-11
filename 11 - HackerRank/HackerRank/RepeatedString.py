def RepeatedString(s,n):
    strLen = len(s)
    numA = 0
    for char in s:
        if char == 'a':
            numA += 1

    times = n // strLen
    residue = n % strLen

    totalA = numA * times

    residueA = 0
    for char in s[:residue]:
        if char == 'a':
            residueA += 1

    return totalA + residueA



s = 'ababa'
n = 3
temp = RepeatedString(s,n)