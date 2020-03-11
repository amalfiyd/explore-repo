def divisibleSumPairs(n, k, ar):
    sets = []
    for i in range(n):
        for j in range(n):
            if i < j and ((ar[i] + ar[j]) % k == 0):
                _set = (ar[i], ar[j])
                sets.append(_set)

    return len(sets)

ar = [1,3,2,6,1,2]
k = 3
n = len(ar)

print(divisibleSumPairs(n,k,ar))