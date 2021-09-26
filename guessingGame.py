import random
number = random.randint(1, 9)
chances = 0

while(chances < 5):
    guess = int(input("Guess a number from 1 to 9: "))
    if(guess > 9 or guess < 1):
        print("Please stay in between 1 and 9")
    if guess == number :
        print("Congratulations! Your guessed correctly")
    elif guess > number :
        print("Your guess is bigger than my number")
    elif guess < number :
        print("Your guess is smaller than my number")
    chances = chances + 1
    
    if chances == 5:
        print("Your Chances Are Completed")
        print('My number Is', number)
