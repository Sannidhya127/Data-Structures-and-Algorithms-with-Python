# The Euclidean Algorithm:

#     gcd(48, 18)

#     Step 1: 48/18 = Qoutient 2 and Remainder 12

#     Step 2: 18/12 = Qoutient 1 and Remainder 6

#     Step 3: 12/6 = Qoutient 2 and Remainder 0

# Therefore the greatest common divisor of 48 and 18 is 6


def gcd(n1, n2):
    if n2 == 0:
        print(n1)
    elif n1 == 0:
        print(n2)
    else:
        gcd(n2, n1 % n2)


gcd(4, 2)
