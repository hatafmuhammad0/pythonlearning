number1 , number2 , number3 = input("Type three numbers seperated by commas : ").split(",")
number1 =int(number1)
number2 =int(number2)
number3 =int(number3)

def greatest (a,b,c):

    if a > (b and c):
        return a
    elif b > (a and c):
        return b
    return c

print(greatest(number1,number2,number3))