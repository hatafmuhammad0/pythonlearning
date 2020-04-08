#define list which will takes input from user a number 
#function that return square of each number input

numbers = input("Please type numbers from 1 to 10 seperated by commas").split(",")


def square (a):
    new_square = []
    for i in a:
        new_square.append(int(i)**2)
    return new_square
        

print(square(numbers))

