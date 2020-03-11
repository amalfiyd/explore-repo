def isPalindrome(input):
    n = len(input) // 2
    for i in range(n):
        if input[i] != input[-(i+1)]:
            return False
    return True

def isPalindromeRec(arr):
    if len(arr) <= 1:
        return True
    if arr[0] != arr[-1]:
        return False

    isPalindromeRec(arr[1:-1])
    return True

