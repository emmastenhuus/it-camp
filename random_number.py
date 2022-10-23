from random import randint

number = randint(1, 100)
guess = 0

found_it = False
max_guesses = int(input("How many guesses do you want? "))
attempts = 0

while attempts < max_guesses and guess != number:
    attempts += 1
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        found_it = True
    elif guess < number:
        print("That's too small.")
    else:
        print("That's too big.")

if found_it:
    print(f"That's correct! You guessed {attempts} times.")
else:
    print("You're an idiot!")
