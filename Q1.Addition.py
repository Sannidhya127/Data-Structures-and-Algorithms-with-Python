# What you have to do: A number of example 54 will be given. You need to break it as 5 and 4 and then add the number. If it is a 3 or 4 digit number like 457, break it as 4, 5,7 and then add them


def add(num):
    if num == 0:
        return 0
    elif "." in str(num):
        print("No decimals please!")
    elif "-" in str(num):
        print("No negative integers please!")
    else:
        return int(num % 10) + add(int(num/10))


print(add(45))
