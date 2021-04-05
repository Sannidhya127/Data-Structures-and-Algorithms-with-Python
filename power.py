def power(n, exp):

    n = int(n)
    exp = int(exp)
    if exp in [0]:
        print(1)
    elif exp == 1:
        print(n)
    else:
        print(n*power(n, exp-1))


power(2, 3)
