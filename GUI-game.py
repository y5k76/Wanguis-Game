import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.max_number = 20
        self.number_to_guess = random.randint(1, self.max_number)
        self.attempts = 0

        self.label = tk.Label(master, text=f"Guess a number between 1 and {self.max_number}")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.reset_button = tk.Button(master, text="New Game", command=self.new_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return

        self.attempts += 1
        if guess < self.number_to_guess:
            self.result_label.config(text="Too low!")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high!")
        else:
            self.result_label.config(text=f"You got it in {self.attempts} tries! 🎉")

    def new_game(self):
        self.number_to_guess = random.randint(1, self.max_number)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
