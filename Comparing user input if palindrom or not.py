#define is_palindrom function that take one work as input 
#Return true if palindrom
#example of palindrom  .... madam -> You read this word from either side

name = input("Type your name : ")

def reverse(a):
    if name[::-1] == a:
        return True
    return False

print(reverse(name)) #Calling function



    


