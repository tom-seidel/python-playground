import random

print("I'm thinking of a number between 1 and 10.")
# secret random number
secret = random.randint(1,10)

# user input
guess = int(input("What's your guess? "))

# check if guess is too high or too low in a loop
while guess != secret:
    if guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("What's your guess? "))
    # if guess is correct
if guess == secret:
    print("You got it!") 
