# My method of finding factorial

num = int(input("Enter the number:"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print("Factorial of a Given Number:", factorial)


def factorialRecursive(n):
    print(n * factorialRecursive(n-1))


factorialRecursive(5)
