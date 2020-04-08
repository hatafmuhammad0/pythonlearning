#define a function which take list as a argument 
#reverse list

fruits = ["apple","banana","orange"]

def rev_fruit(x):
    new_fruits = []
    i = 0
    while i < (len(x) +2) :
        new_fruits.append(x.pop())
        i += 1
    return new_fruits

print(rev_fruit(fruits))