#Modify Number game 
import random

winning_number = random.randint(1,10)
guess_number = int(input("Type Guess Number : "))
times = 1
game_over = False
while not game_over:
    if guess_number == winning_number:
        print(f"You win and you guess number in {times} times")
        game_over = True
    else: 
        if guess_number < winning_number:
            print("Too low")
        else:
            print("Too High")
    times += 1
    guess_number = int(input("Try again"))
