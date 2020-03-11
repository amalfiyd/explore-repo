def bonAppetite(bill, k, b):
    b_actual = 0
    n = len(bill)
    for i in range(n):
        if i != k:
            b_actual += bill[i]

    b_actual = int(b_actual / 2)
    b_charged = b

    charge = b_charged - b_actual
    if charge > 0:
        print(str(charge))
        return

    print('Bon Appetit')
    return

bill = [3,10,2,9]
k = 1
b = 12

bonAppetite(bill, k, b)