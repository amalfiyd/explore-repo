def chocolateFeast(n, c, m):
    initChoc = n // c
    countEat = initChoc
    wraps = initChoc

    while wraps // m > 0:
        # print("before",wraps)
        wraps = wraps - m + 1
        # print('after', wraps)
        countEat += 1

    return countEat

n = 6
c = 2
m = 2

temp = chocolateFeast(n,c,m)