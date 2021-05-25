import random

guesses_taken = 0


name = input("Hello! What is your name?: ")
number = random.randint(1, 20)
print(f"I'm thinking of a number between 1 - 20, try guess it {name}!")

while guesses_taken < 6:
    print("Take a guess")
    guess = int(input())
    guesses_taken += 1
    

    if guess < number:
        print("your guess is too low:(")
    if guess > number:
        print("your guess is too high :(")
    if guess == number:
        print("you guessed it! it was", number)
        break

if guess != number:
    number = str(number)
    print("Too bad. It was", number)
