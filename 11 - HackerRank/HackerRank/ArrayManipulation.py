def arrayManipulation(n, queries):
    numHits = [0 for x in range(n + 1)]
    for query in queries:
        start = query[0]
        end = query[1]
        value = query[2]
        print(start, end+1, value)
        for i in range(start, end + 1):
            numHits[i] += value

    return max(numHits)

n = 10
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

temp = arrayManipulation(n, queries)


