temp = "test"
temp[0] = 'p'
print(temp)

# The Importance of immutability
"""
The immutability feature is important for at least these reasons:
    It make multi-threaded[1] computation safer
    It makes distributed[2] computation safer
    It forces a single source of truth[3]
"""
