# Main function
def birthday(s, d, m):
    counter = 0
    n = len(s)
    for i in range(n-m+1):
        _start = i
        _end = i + m
        subset = s[_start:_end]
        print(subset)
        if sum(subset) == d:
            counter += 1

    return counter

s = [1,2,3,4,5]
d = 4
m = 4

birthday(s,d,m)

