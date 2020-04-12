#define a function
#input
#num,iterable(list) containing numbers as args

#example
#nums =[1,2,3]
#to power (3, *nums)

#output 
#list ---> [1,8,27]

#if user didn't pass any args then give user a message 'hey you didn't pass"

#else return list

numbers = list(map(int,input("Type numbers seperated by commas").split(",")))#List


def powers (x ,*args):
    output = []
    if args:
        return [i**x for i in args]
    else:
        print("Hey you didn't pass args")
    

print(powers(2,*numbers))