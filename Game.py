import random

def main():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    main()
