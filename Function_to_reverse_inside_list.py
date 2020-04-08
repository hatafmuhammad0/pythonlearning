#define a function that take list of words 
#function will reverse the words inside a list 

Numbers = [[1,2,3],[4,5,6],[7,8,9]]


def reverse (x):
    new_numbers = []
    for i in range(len(x)):
        for y in range (len(x)):
            new_numbers.append(x[i].pop())
    return new_numbers

print(reverse(Numbers))