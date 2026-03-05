import tkinter as tk
from tkinter import ttk
import random

class GuessGameGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x500')
        self.root.title('Number Guessing Game (SHAMS)')

        self.label_instruction = tk.Label(self.root, text='Select difficulty:')
        self.label_instruction.pack(pady=10)

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set('10 Guesses')  # Default difficulty
        self.difficulty_menu = ttk.Combobox(self.root, textvariable=self.difficulty_var, values=['10 Guesses (Easy)', '5 Guesses (Normal)', '3 Guesses (Hard)'])
        self.difficulty_menu.pack(pady=10)

        self.button_start = tk.Button(self.root, text='Start Game', command=self.start_game)
        self.button_start.pack(pady=10)

        self.label_result = tk.Label(self.root, text='')
        self.label_result.pack(pady=10)

        

        self.root.mainloop()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        max_guesses = int(difficulty.split()[0])

        self.initialize_game(max_guesses)

        self.label_instruction.config(text='Guess the number between 1 and 100:')
        self.difficulty_menu.config(state=tk.DISABLED)
        self.button_start.config(state=tk.DISABLED)

        self.entry_guess = tk.Entry(self.root)
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(self.root, text='Submit Guess', command=self.check_guess)
        self.button_guess.pack(pady=10)

        self.button_replay = tk.Button(self.root, text='Replay', command=self.replay_game)
        self.button_replay.pack(pady=10)
        self.button_replay.pack_forget()  # Initially hide the replay button

    def initialize_game(self, max_guesses):
        self.jackpot = random.randint(1, 100)
        self.max_guesses = max_guesses
        self.counter = 0
        self.is_winner = False

    def check_guess(self):
        if self.is_winner:  # If the game is already won, ignore further guesses
            return

        user_guess = int(self.entry_guess.get())
        self.counter += 1

        if user_guess < self.jackpot:
            message = 'Guess higher!'
        elif user_guess > self.jackpot:
            message = 'Guess lower!'
        else:
            self.display_result(True)
            return

        if self.counter < self.max_guesses:
            message += f' You have {self.max_guesses - self.counter} chances left.'
        else:
            self.display_result(False)
            return

        self.label_result.config(text=message)

    def display_result(self, is_winner):
        self.is_winner = is_winner
        if is_winner:
            result_message = f'Congratulations! You won in {self.counter} attempts.'
        else:
            result_message = f'Sorry, you lost. The correct number was {self.jackpot}.'

        self.label_result.config(text=result_message)
        self.button_guess.config(state=tk.DISABLED)
        self.button_replay.pack()  # Display the replay button

    def replay_game(self):
        self.label_instruction.config(text='Select difficulty:')
        self.difficulty_menu.config(state=tk.NORMAL)
        self.button_start.config(state=tk.NORMAL)

        self.entry_guess.destroy()
        self.button_guess.destroy()
        self.button_replay.destroy()

        self.label_result.config(text='')

if __name__ == "__main__":
    GuessGameGUI()

