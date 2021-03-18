import sys

# sys.setrecursionlimit(5000)

# My method of finding factorial


def factorial():
    num = int(input("Enter the number:"))
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i

    print("Factorial of a Given Number:", factorial)


def factorialRecursive(n):
    # assert n>=0 and int(n) == n, "The number has to be a positive integer"  (Can use this instead of the elif also)
    if n in [0, 1]:
        return 1
    elif n < 0:
        print("Can't find factorial of negative integers")
    elif "." in str(n):
        print("No decimal integer supported")
    else:
        return n * factorialRecursive(n-1)


print(factorialRecursive(4))
factorial()
