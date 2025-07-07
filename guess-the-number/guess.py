import random

print("I'm thinking of a number between 1 and 10.")
# secret random number
secret = random.randint(1,10)
 
while True:
    # check if guess is a number
    try:
        guess = int(input("What's your guess? "))
    except ValueError:
        print("That's not a valid number! Please try again.")
        continue
    #check if guess is between 1 and 10
    if guess < 1 or guess > 10:
        print("The number must be between 1 and 10! Please try again.")
        continue
    # number is too high or too low
    if guess > secret:
        print("Too high! Try again.")
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("You got it!") # guess is correct
        break
