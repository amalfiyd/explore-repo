def RansomNotes(magazine, note):
    wordDict = {}
    for word in magazine:
        if word in wordDict.keys():
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    for word in note:
        if word not in wordDict.keys():
            print("No")
            return
        else:
            if wordDict[word] == 0:
                print("No")
                return
        wordDict[word] -= 1

    print("Yes")
    return