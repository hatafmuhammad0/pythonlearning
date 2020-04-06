#take 2 numbers in input

number1 , number2 = input("Type two numbers seperated by commas : ").split(",")

def greatest(a,b):
    if a > b:
        return a
    return b

print(greatest(int(number1),int(number2)))