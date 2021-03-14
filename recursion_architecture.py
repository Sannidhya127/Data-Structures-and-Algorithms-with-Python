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


# def add(n1, n2):
#     sum = n1+n2
#     print(sum)


# add(74, 74)

firstmethod()
recursiveMethod(995)


# ** Explanations:

# firstmethod(), secondmethod(), thirdmethod(), fourthmethod(): This is a very simple recursive approach. The basic thing is that the firstmethod() when run calles the secondmethod() and then prints "This is first method". Now, when the firstmethod calls the secondmethod, the secondmenthod also calls the thirdmethod() and prints "I am the second method". Now when the thirdmethod is called it also calls the fourthmethod() and prints "I am the third method". The fourthmethod at the end prints "I am the fourth method". In the following code we therefore see that everytime a function is run it has to pause itself, run the functon it calls and then complete it and print the statement (exc: fourthmethod() as it does not call any further function). If you run the code you will see the output like this:

#	This is the fourth method
#	This is the third method
#	This is the second method
#	This is the first method

# It first runs the corresponding function it calls and then returns tp itself and prints the statement

# recursiveMethod(n): This is a the best example to show if someone asks for some code example of recursive method. It is very simple. The function recursiveMethod(n) takes in a number 'n'. For simplicity lets suppose that the number is 5. Now the first thing it does is checks it 5 is lesser than 1. Ofcourse it is false. So it moves to the else part where it makes a new variable newN which is n-1, i.e, 5-1 or 4 and it calls the recursiveMethod(newN) with the new variable with value 4. The fucntion again chacks if it is less than 1, but it isn't so. So it repeats itseld untill the value of newN is 0. This is the simplest form  of recursion used for solving problems
