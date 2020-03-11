def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif year < 1918:
        if year % 4 == 0:
            # leap year julian
            return '12.09.' + str(year)
        else:
            # non leap year julian
            return '13.09.' + str(year)
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            # leap year georgian
            return '12.09.' + str(year)

        else:
             # non leap year georgian
            return '13.09.' + str(year)

test = dayOfProgrammer(2000)
print(test)