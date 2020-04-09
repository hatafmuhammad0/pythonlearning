#Create a function which return the number of list with in the list 

number = [1,2,3,[4,5,6],[7,8,9],[11,12,13,15],19,20]



def listing (x):
    a = []
    for i in x:
        b = i
        if type(i) == list:
            a.append(b)
        else:
            pass
    return len(a)

print(listing(number))

