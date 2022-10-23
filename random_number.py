from random import randint

number = randint(1, 100)
guess = 0

while guess != number:
    number_of_guesses = int(input("How many guesses do you want? "))
    for i in range(number_of_guesses):
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print(f"That's correct! You guessed {i} times.")
        elif guess < number:
            print("That's too small.")
        else:
            print("That's too big.")
    break
print("You're an idiot!")