import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Guess the Number")

        # --- Game Variables ---
        self.levels = {
            "Easy": 10,
            "Medium": 20,
            "Hard": 50
        }
        self.level = tk.StringVar(value="Easy")
        self.max_attempts = 5
        self.score = 0
        self.attempts = 0
        self.max_number = self.levels[self.level.get()]

        # --- UI Elements ---
        self.title_label = tk.Label(master, text="🎯 Guess the Number!", font=("Arial", 16, "bold"), fg="navy")
        self.title_label.pack(pady=10)

        # Difficulty dropdown
        self.level_menu = tk.OptionMenu(master, self.level, *self.levels.keys(), command=self.set_level)
        self.level_menu.pack()

        # Score display
        self.score_label = tk.Label(master, text=f"🏆 Score: {self.score}", font=("Arial", 12, "bold"), fg="darkgreen")
        self.score_label.pack(pady=5)

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

        self.set_level("Easy")

    # --- Game Logic ---
    def set_level(self, level):
        """Change difficulty level and reset game."""
        self.max_number = self.levels[level]
        self.new_game()

    def new_game(self):
        """Start or reset a round."""
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
        """Check the player's guess and handle scoring."""
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="❌ Please enter a valid number.", fg="red")
            return

        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(
                text=f"⬇️ Too low! Attempts left: {self.max_attempts - self.attempts}", fg="orange"
            )
        elif guess > self.number_to_guess:
            self.result_label.config(
                text=f"⬆️ Too high! Attempts left: {self.max_attempts - self.attempts}", fg="orange"
            )
        else:
            # 🎉 Player wins — calculate bonus based on remaining attempts
            bonus = max(0, (self.max_attempts - self.attempts + 1) * 10)
            self.score += bonus
            self.score_label.config(text=f"🏆 Score: {self.score}")
            self.result_label.config(
                text=f"🎉 You got it in {self.attempts} tries! +{bonus} points!", fg="green"
            )
            self.end_game()
            return

        # 💀 Check for loss
        if self.attempts >= self.max_attempts:
            self.result_label.config(
                text=f"💀 Out of attempts! The number was {self.number_to_guess}. No points this round.",
                fg="red"
            )
            self.end_game()

    def end_game(self):
        """Disable input after win/loss."""
        self.entry.config(state="disabled")
        self.button.config(state="disabled", bg="gray")

# --- Run the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("420x370")
    game = GuessNumberGame(root)
    root.mainloop()
