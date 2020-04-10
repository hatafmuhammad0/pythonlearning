#taking input from user and create a dictionary of it

name = input("Type your name: ")
age = int(input("Type your age: "))
movies = input("Type your favorite movies seperated by commas : ").split(",")



def user_info (a,b,c):
    user_info = {
        'name' : a,
        'age' : b,
        'movies' :c
    }
    return user_info

print(user_info(name,age,movies))
