import random

def choose_difficulty():
    print("Select difficulty: easy, medium, or hard")
    while True:
        choice = input("Enter choice: ").lower()
        if choice == "easy":
            return 10
        elif choice == "medium":
            return 20
        elif choice == "hard":
            return 50
        else:
            print("Invalid choice, please try again.")

def main():
    max_number = choose_difficulty()
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    print(f"I'm thinking of a number between 1 and {max_number}.")

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
            print(f"You got it in {attempts} tries! 🎉")
            break

if __name__ == "__main__":
    main()
