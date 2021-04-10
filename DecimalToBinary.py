# The Process:

# step 1 : Divide the number by 2
# step 2 : Get the integer qoutient for the next iteration
# step 3 : Get the remainder for the binary digit
# step 4 : Repeat the steps until qoutient is 0


def DecimalToBinary(num):
    if num == 0:
        return ""
    # elif num == 1:
    #     print("It's 1!")
    else:
        modulus = divmod(num, 2)
        eula = num//2
        print(DecimalToBinary(eula), modulus[1], end='')
        return ""


        # print(modulus[1])
DecimalToBinary(53)
