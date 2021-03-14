def poweroftwo(n):
    if n == 0:
        return 1
        # return "done"
    else:
        nth = n-1
        power = poweroftwo(nth)
        # print(int(power) * 2)
        print(power*2)


# poweroftwo(3)


def powerOftwoIter(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i+1
    print(power)


powerOftwoIter(8)
