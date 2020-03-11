def larrysArray(ar):
    probIx = 0
    for ix, val in enumerate(ar):
        if ix + 1 != val:
            probIx = ix

            # problem's found
            subset = ar[probIx: probIx + 3]

def lookForEl(el, arr, probIx):
    i = 0
    subset = arr[i+probIx: i+probIx + 3]

