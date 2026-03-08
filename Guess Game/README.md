# Number Guessing Game

## Project Overview

This project is a graphical Number Guessing Game implemented in Python using the Tkinter library. The application generates a random number between 1 and 100, and the player must guess the correct number within a limited number of attempts determined by the selected difficulty level.

The program provides feedback after each guess to guide the player until the number is guessed correctly or the maximum number of attempts is reached.

## Features

* Graphical user interface implemented using Tkinter
* Random number generation using Python's random module
* Multiple difficulty levels
* Real-time feedback indicating whether the correct number is higher or lower
* Display of remaining attempts
* Win or loss result display
* Option to restart the game

## Difficulty Levels / can be changed also 

* Easy – 10 guesses
* Normal – 5 guesses
* Hard – 3 guesses

## How the Game Works

1. The user selects a difficulty level from the interface.
2. The program generates a random number between 1 and 100.
3. The user enters guesses through the input field.
4. After each guess, the program indicates whether the correct number is higher or lower.
5. The game ends when the user guesses the correct number or when all attempts are used.

## Project Structure

```
guess.py
README.md
```

* `guess.py` contains the complete implementation of the graphical game interface and game logic. 

## Requirements

Python 3.x

Tkinter is included with most standard Python installations.

## Running the Program

Navigate to the project directory and execute the following command:

```
python guess.py
```

The graphical interface will open and the game can be started from the application window.

## Technologies Used

* Python
* Tkinter
* Random module
