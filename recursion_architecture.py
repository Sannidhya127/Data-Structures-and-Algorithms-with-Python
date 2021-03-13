# vscode-tabify.tabify


def firstmethod():
    secondmethod()
    print("This is the first method")


def secondmethod():
    thirdmethod()
    print("This is the second method")


def thirdmethod():
    fourthmethod()
    print("This is the third method")


def fourthmethod():
    print("This is the fourth method")


def recursiveMethod(n):
    if n < 1:
        print(f"{n} is less than 1")
    else:
        newN = n-1
        recursiveMethod(newN)


# if __name__ == ' __main__':
    # firstmethod()
recursiveMethod(995)
