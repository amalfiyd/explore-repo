def jumpingOnClouds(c):
    curIx = 0
    jumpCounter = 0
    while curIx < len(c) - 1:
        if curIx + 2 >= len(c):
            curIx += 1
            jumpCounter += 1
        else:
            if c[curIx + 2] == 0:
                curIx += 2
                jumpCounter += 1
            elif c[curIx + 1] == 0:
                curIx += 1
                jumpCounter += 1
            else:
                print("No solution")

        print("curIx", curIx)

    return jumpCounter

c = [0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0]
print(c)
jumpingOnClouds(c)