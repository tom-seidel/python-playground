import random

print("I'm thinking of a number between 1 and 10.")
#secret random number
secret = random.randint(1,10)

#user input
guess = int(input("What's your guess? "))

#check if guess is correct
if guess == secret:
    print("You got it!")
else:
    print("Nope. The number I was thinking of was", secret)
