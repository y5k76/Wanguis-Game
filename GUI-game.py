import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Guess the Number")

        # --- Game variables ---
        self.levels = {
            "Easy": (10, 5),
            "Medium": (20, 7),
            "Hard": (50, 10)
        }
        self.level = tk.StringVar(value="Easy")

        # --- UI Elements ---
        self.title_label = tk.Label(master, text="🎯 Guess the Number!", font=("Arial", 16, "bold"), fg="navy")
        self.title_label.pack(pady=10)

        # Difficulty dropdown
        self.level_menu = tk.OptionMenu(master, self.level, *self.levels.keys(), command=self.set_level)
        self.level_menu.pack()

        self.info_label = tk.Label(master, text="", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.button = tk.Button(master, text="Guess", command=self.check_guess, bg="lightgreen")
        self.button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.reset_button = tk.Button(master, text="New Game", command=self.new_game, bg="lightblue")
        self.reset_button.pack(pady=10)

        # Start first game
        self.set_level("Easy")

    def set_level(self, level):
        self.max_number, self.max_attempts = self.levels[level]
        self.new_game()

    def new_game(self):
        self.number_to_guess = random.randint(1, self.max_number)
        self.attempts = 0
        self.result_label.config(text="", fg="black")
        self.info_label.config(
            text=f"Level: {self.level.get()} | Guess a number between 1 and {self.max_number}\nYou have {self.max_attempts} attempts!"
        )
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.button.config(state="normal", bg="lightgreen")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="❌ Please enter a valid number.", fg="red")
            return

        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text=f"⬇️ Too low! Attempts left: {self.max_attempts - self.attempts}", fg="orange")
        elif guess > self.number_to_guess:
            self.result_label.config(text=f"⬆️ Too high! Attempts left: {self.max_attempts - self.attempts}", fg="orange")
        else:
            self.result_label.config(text=f"🎉 You got it in {self.attempts} tries! You win! 🎉", fg="green")
            self.end_game()
            return

        if self.attempts >= self.max_attempts:
            self.result_label.config(
                text=f"💀 Out of attempts! The number was {self.number_to_guess}.", fg="red"
            )
            self.end_game()

    def end_game(self):
        """Disable input after win/loss."""
        self.entry.config(state="disabled")
        self.button.config(state="disabled", bg="gray")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x350")
    game = GuessNumberGame(root)
    root.mainloop()
