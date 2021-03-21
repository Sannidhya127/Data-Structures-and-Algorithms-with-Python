import sys

sys.setrecursionlimit(5000)


def fibonacci(n):
    # assert n >= 0 and int(n) == n, "The number has to be a positive integer"
    if n in [0, 1]:
        return n
    elif "." in str(n):
        print("The number cannot be a decimal")
    elif "-" in str(n):
        print("The number has to be a positive integer")

    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))
