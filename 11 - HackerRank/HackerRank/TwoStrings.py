def TwoStrings(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 >= n2:
        temp = {}
        for char in s1:
            if char not in temp.keys():
                temp[char] = 1
            else:
                temp[char] += 1

        for char in s2:
            if char in temp.keys():
                return "YES"

        return "NO"
    else:
        temp = {}
        for char in s2:
            if char not in temp.keys():
                temp[char] = 1
            else:
                temp[char] += 1

        for char in s1:
            if char in temp.keys():
                return "YES"

        return "NO"

s1 = 'hello'
s2 = 'world'
print(TwoStrings(s1,s2))